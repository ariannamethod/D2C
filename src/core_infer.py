import argparse
import torch
from logger import log_event, log_failure
from model import AutoModelForCausalLM, AutoTokenizer


def generate(start: str, num_tokens: int, checkpoint: str | None = None) -> str:
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint or "")
        model = AutoModelForCausalLM.from_pretrained(checkpoint or "")
        model.to("cpu")
        model.eval()
        idx = tokenizer.encode(start)
        inp = torch.tensor([idx], dtype=torch.long)
        with torch.no_grad():
            out = model.generate(inp, num_tokens)
        text = tokenizer.decode(out[0])
        log_event("generated text")
        return text
    except Exception as e:
        log_failure(str(e))
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate text with D2C")
    parser.add_argument("--start", default="\n")
    parser.add_argument("--num_tokens", type=int, default=50)
    parser.add_argument("--checkpoint", type=str)
    args = parser.parse_args()
    text = generate(args.start, args.num_tokens, args.checkpoint)
    print(text)


if __name__ == "__main__":
    main()
