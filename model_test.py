
from transformers import pipeline

MODEL_NAME = "deepset/roberta-base-squad2"

print("Loading model...")

qa_pipeline = pipeline(
    "question-answering",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME
)

print("Model loaded successfully!")

context = """
Python was created by Guido van Rossum.
It was first released in 1991.
Python is a high-level, general-purpose programming language.
"""

question = "Who is Vinh Kiet?"

result = qa_pipeline(
    question=question,
    context=context
)

print("\nQuestion:", question)
print("Answer:", result["answer"])
print("Confidence:", result["score"])
print("Start position:", result["start"])
print("End position:", result["end"])
