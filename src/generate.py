import argparse
import torch
from model import GPT, GPTConfig


def main():
    parser = argparse.ArgumentParser(description="Generate using DeepSeek model without HF")
    parser.add_argument('--checkpoint', type=str, required=False, help='path to model checkpoint')
    parser.add_argument('--start', type=str, default="\n", help='start prompt')
    parser.add_argument('--num_tokens', type=int, default=50)
    args = parser.parse_args()

    config = GPTConfig()
    model = GPT(config)
    if args.checkpoint:
        state = torch.load(args.checkpoint, map_location='cpu')
        model.load_state_dict(state)
    model.eval()

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)

    idx = torch.tensor([[ord(c) % config.vocab_size for c in args.start]], dtype=torch.long, device=device)
    with torch.no_grad():
        out = model.generate(idx, args.num_tokens)
    text = ''.join(chr(int(i)) for i in out[0].tolist())
    print(text)


if __name__ == '__main__':
    main()
