
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline


MODEL_NAME = "deepset/roberta-base-squad2"


# Load the model when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading QA model...")

    app.state.qa_pipeline = pipeline(
        "question-answering",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME
    )

    print("QA model loaded successfully!")

    yield

    print("Application shutting down...")


app = FastAPI(
    title="Question Answering API",
    description="An API powered by RoBERTa for extractive question answering.",
    version="1.0.0",
    lifespan=lifespan
)


# Define the expected input JSON structure
class QARequest(BaseModel):
    question: str = Field(min_length=1, max_length=500)
    context: str = Field(min_length=1, max_length=10000)


# GET /
@app.get("/")
def root():
    return {
        "message": "Welcome to the Question Answering API",
        "model": MODEL_NAME,
        "endpoint": "/predict"
    }


# GET /health
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": hasattr(app.state, "qa_pipeline")
    }


# POST /predict
@app.post("/predict")
def predict(request: QARequest):

    question = request.question.strip()
    context = request.context.strip()

    if not question or not context:
        raise HTTPException(
            status_code=422,
            detail="Question and context cannot be empty."
        )

    try:
        result = app.state.qa_pipeline(
            question=question,
            context=context
        )

        return {
            "question": question,
            "answer": result["answer"],
            "confidence": float(result["score"]),
            "start": result["start"],
            "end": result["end"],
            "model": MODEL_NAME
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Model inference failed."
        ) from e
