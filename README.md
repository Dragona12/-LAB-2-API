# Question Answering API

## 1. Student Information

- **Full name:** Võ Phi Long
- **Student ID:** 25127210
- **Course:** Computational Thinking
- **Lab:**  [LAB-2] API

## 2. Selected Hugging Face Model

- **Model:** `deepset/roberta-base-squad2`
- **Model link:** https://huggingface.co/deepset/roberta-base-squad2
- **Task:** Extractive Question Answering

This project uses a pretrained RoBERTa model fine-tuned on the SQuAD 2.0 dataset to answer questions based on user-provided text.

## 3. Project Description

This project implements a Question Answering Web API using FastAPI and Hugging Face Transformers.

Users provide:
- A question they want to ask.
- A context containing relevant information.

The API processes these inputs using the pretrained RoBERTa model and returns the predicted answer, confidence score, and answer position in JSON format.

## 4. Project Structure

```text
qa-api-lab/
├── main.py
├── model_test.py
├── test_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `main.py`: FastAPI application and API endpoints.
- `model_test.py`: Standalone model inference test.
- `test_api.py`: Automated API testing using Python requests.
- `requirements.txt`: Project dependencies.

## 5. Installation

### Requirements

- Python 3.14
- pip

### Step 1: Clone the repository

```bash
git clone https://github.com/Dragona12/-LAB-2-API.git
cd qa-api-lab
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
``` 

you may encounter some problems Powershell may prevent the activation virtual environment. To acknowledge more about this [python doc about venv](https://docs.python.org/3/library/venv.html). Or simply use below scripts to enable:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```



### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

- API root: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

The model is automatically downloaded and loaded during application startup if it is not already cached.

## 7. API Usage

### GET /

Returns a brief introduction to the API.

### GET /health

Checks whether the application is running and the model has been loaded.

Example response:

```json
{
    "status": "ok",
    "model_loaded": true
}
```

### POST /predict

Receives a question and its corresponding context.

Example request:

```json
{
    "question": "Who created Python?",
    "context": "Python was created by Guido van Rossum. It was first released in 1991."
}
```

Example response structure:

```json
{
    "question": "Who created Python?",
    "answer": "Guido van Rossum",
    "confidence": 0.98,
    "start": 25,
    "end": 41,
    "model": "deepset/roberta-base-squad2"
}
```

*The confidence score and answer positions above are illustrative.*

## 8. Testing

Make sure the API server is running, then open another terminal and execute:

```bash
python test_api.py
```

The testing script covers:
- Root endpoint.
- Health endpoint.
- Question answering with two different inputs.
- Invalid input validation.

## 9. Demonstration Video

**Video link:** [text](url)

The video demonstrates:
- Introduction to the selected Hugging Face model.
- Source code structure.
- Running the FastAPI application.
- Testing the API with at least two different inputs.
- Explanation of the returned results.
