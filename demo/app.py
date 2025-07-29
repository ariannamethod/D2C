import gradio as gr
import torch
from model import GPT, GPTConfig

config = GPTConfig()
model = GPT(config)
model.eval()
DEVICE = 'cpu'
model.to(DEVICE)


def generate(message: str, chat_history: list, system_prompt: str, max_new_tokens: int = 64,
             temperature: float = 1.0, top_p: float = 0.9, top_k: int = 50,
             repetition_penalty: float = 1.0):
    idx = torch.tensor([[ord(c) % config.vocab_size for c in message]], dtype=torch.long, device=DEVICE)
    with torch.no_grad():
        out = model.generate(idx, max_new_tokens, temperature=temperature, top_k=top_k)
    text = ''.join(chr(int(i)) for i in out[0].tolist())
    return text

chat_interface = gr.ChatInterface(
    fn=generate,
    additional_inputs=[
        gr.Textbox(label="System prompt", lines=1),
        gr.Slider(label="Max new tokens", minimum=1, maximum=256, step=1, value=64),
        gr.Slider(label="Temperature", minimum=0, maximum=2.0, step=0.1, value=1.0),
        gr.Slider(label="Top-p", minimum=0.05, maximum=1.0, step=0.05, value=0.9),
        gr.Slider(label="Top-k", minimum=1, maximum=1000, step=1, value=50),
        gr.Slider(label="Repetition penalty", minimum=1.0, maximum=2.0, step=0.05, value=1.0),
    ],
    stop_btn=None,
)

if __name__ == '__main__':
    chat_interface.launch()
