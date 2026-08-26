# Emotion Detector - Final Project

This application is an AI-based Web Application for Emotion Detection built using Python, Flask, and IBM Watson NLP. It analyzes user-provided text and identifies the scores for emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**, along with determining the **dominant emotion**.

## Project Tasks & Architecture

- **Task 1**: Repository initialization and documentation (`README.md`).
- **Task 2 & 3**: Emotion Detection module (`EmotionDetection/emotion_detection.py`) querying Watson NLP API and formatting outputs.
- **Task 4**: Python Package bundling (`EmotionDetection/__init__.py`).
- **Task 5**: Unit testing framework (`test_emotion_detection.py`).
- **Task 6 & 7**: Flask Web deployment (`server.py`) with error handling for status code 400 / blank inputs.
- **Task 8**: Static Code Analysis compliance (`pylint server.py` score: 10/10).

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd "course_era assignment"
   ```

2. **Install dependencies**:
   ```bash
   pip install requests flask pylint
   ```

## Running Unit Tests

Execute unit tests to verify emotion detection accuracy:
```bash
python3 test_emotion_detection.py
```

## Running Static Code Analysis

Ensure code quality adhering to PEP8 standards:
```bash
pylint server.py
```

## Running the Web Application

Start the Flask web server:
```bash
python3 server.py
```
Open your browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`.
