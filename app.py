from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.core_infer import generate

app = FastAPI()

# Enable CORS for all origins to allow cross-domain requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    start: str = "\n"
    num_tokens: int = 50
    checkpoint: str | None = None


class GenerateResponse(BaseModel):
    text: str


@app.post("/generate", response_model=GenerateResponse)
def generate_endpoint(req: GenerateRequest) -> GenerateResponse:
    text = generate(req.start, req.num_tokens, req.checkpoint)
    return GenerateResponse(text=text)


@app.get("/")
def read_root() -> dict:
    return {"status": "ok"}
