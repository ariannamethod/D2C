import argparse
import json
import torch
from torch.utils.data import Dataset, DataLoader
from pathlib import Path

from model import GPT, GPTConfig

class JsonDataset(Dataset):
    def __init__(self, path):
        path = Path(path)
        with open(path, 'r', encoding='utf-8') as f:
            self.data = [json.loads(line) for line in f if line.strip()]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        text = item.get('instruction', '') + item.get('output', '')
        ids = torch.tensor([ord(c) % 256 for c in text], dtype=torch.long)
        return ids, ids.clone()


def main():
    parser = argparse.ArgumentParser(description='Train DeepSeek model without HF')
    parser.add_argument('--data', required=True, help='path to training jsonl')
    parser.add_argument('--epochs', type=int, default=1)
    parser.add_argument('--lr', type=float, default=3e-4)
    args = parser.parse_args()

    config = GPTConfig()
    model = GPT(config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)
    dataset = JsonDataset(args.data)
    loader = DataLoader(dataset, batch_size=1, shuffle=True)

    model.train()
    for _ in range(args.epochs):
        for x, y in loader:
            logits, loss = model(x, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


if __name__ == '__main__':
    main()
