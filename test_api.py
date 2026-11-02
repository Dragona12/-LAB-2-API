
import requests

BASE_URL = "http://127.0.0.1:8000"


def test_root():
    response = requests.get(f"{BASE_URL}/")

    print("\n--- GET / ---")
    print("Status:", response.status_code)
    print(response.json())

    assert response.status_code == 200


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    print("\n--- GET /health ---")
    print("Status:", response.status_code)
    print(response.json())

    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict(question, context):
    response = requests.post(
        f"{BASE_URL}/predict",
        json={
            "question": question,
            "context": context
        }
    )

    print("\n--- POST /predict ---")
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    assert response.json()["answer"] != ""


def test_invalid_input():
    response = requests.post(
        f"{BASE_URL}/predict",
        json={
            "question": "",
            "context": "Python is a programming language."
        }
    )

    print("\n--- Invalid input test ---")
    print("Status:", response.status_code)
    print(response.json())

    assert response.status_code == 422


if __name__ == "__main__":

    test_root()

    test_health()

    # Test case 1
    test_predict(
        question="Who created Python?",
        context="Python was created by Guido van Rossum. "
                "It was first released in 1991."
    )

    # Test case 2
    test_predict(
        question="What is the capital of France?",
        context="Paris is the capital of France. "
                "France is located in Western Europe."
    )

    # Test invalid input
    test_invalid_input()

    print("\nAll API tests passed!")
