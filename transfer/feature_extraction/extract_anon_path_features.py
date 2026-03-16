from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
import torch

from transfer.pattern_tokenizer import PatternTokenizer


def extract_anonymous_path_features(
    edge_index: torch.Tensor,
    x: torch.Tensor,
    *,
    start_nodes: list[int] | None = None,
    walk_length: int = 8,
    walks_per_node: int = 64,
    p: float = 1.0,
    q: float = 1.0,
    directed: bool = True,
    seed: int = 42,
) -> tuple[torch.Tensor, list[str], dict]:
    tokenizer = PatternTokenizer(
        walk_length=walk_length,
        walks_per_node=walks_per_node,
        p=p,
        q=q,
        directed=directed,
        seed=seed,
    )
    result = tokenizer.tokenize(edge_index=edge_index, x=x, start_nodes=start_nodes)

    walks = result.walks.cpu().numpy()
    num_nodes = walks.shape[0]
    seq_len = walks.shape[2]

    feature_names = (
        ["cycle_participation", "chain_length_mean"]
        + [f"revisit_hist_{k}" for k in range(seq_len)]
        + ["walk_valid_mask"]
    )
    features = np.zeros((num_nodes, len(feature_names)), dtype=np.float32)

    for i in range(num_nodes):
        node_walks = walks[i]
        cycle_hits = 0.0
        unique_lengths: list[float] = []
        revisit_hist = np.zeros(seq_len, dtype=np.float32)
        valid_walks = 0

        for walk in node_walks:
            unique_count = len(np.unique(walk))
            revisits = int(walk.size - unique_count)
            revisits = min(revisits, seq_len - 1)
            revisit_hist[revisits] += 1.0
            unique_lengths.append(float(unique_count))
            if np.any(walk[1:] == walk[0]):
                cycle_hits += 1.0
            if unique_count > 1:
                valid_walks += 1

        total_walks = max(float(len(node_walks)), 1.0)
        revisit_hist /= total_walks
        features[i, 0] = cycle_hits / total_walks
        features[i, 1] = float(np.mean(unique_lengths))
        features[i, 2 : 2 + seq_len] = revisit_hist
        features[i, -1] = valid_walks / total_walks

    metadata = {
        "num_nodes": int(num_nodes),
        "walk_length": walk_length,
        "walks_per_node": walks_per_node,
        "directed": directed,
        "seed": seed,
        "feature_names": feature_names,
        "start_nodes": start_nodes if start_nodes is not None else "all",
    }
    return torch.from_numpy(features), feature_names, metadata


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract anonymous path features")
    parser.add_argument("--edge-index", required=True)
    parser.add_argument("--node-features", required=True)
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument("--output-dir", default="transfer/outputs")
    parser.add_argument("--walk-length", type=int, default=8)
    parser.add_argument("--walks-per-node", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--start-node-count", type=int, default=0)
    args = parser.parse_args()

    edge_index = torch.load(args.edge_index)
    x = torch.load(args.node_features)
    start_nodes = None
    if args.start_node_count > 0:
        start_nodes = list(range(min(args.start_node_count, int(x.shape[0]))))

    features, feature_names, metadata = extract_anonymous_path_features(
        edge_index=edge_index,
        x=x,
        start_nodes=start_nodes,
        walk_length=args.walk_length,
        walks_per_node=args.walks_per_node,
        seed=args.seed,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    pt_path = output_dir / f"{args.output_prefix}.pt"
    csv_path = output_dir / f"{args.output_prefix}.csv"
    manifest_path = output_dir / f"{args.output_prefix}_metadata_manifest.json"

    torch.save(
        {
            "features": features,
            "feature_names": feature_names,
            "metadata": metadata,
        },
        pt_path,
    )

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["node_id", *feature_names])
        for idx, row in enumerate(features.tolist()):
            writer.writerow([idx, *row])

    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(pt_path)
    print(csv_path)
    print(manifest_path)


if __name__ == "__main__":
    main()
