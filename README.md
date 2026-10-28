# AI381 Lab 2 — MLOps

[![AI381 Lab 2 CI](https://github.com/safaazreqat69-gif/AI381_Lab2/actions/workflows/ci.yml/badge.svg)](https://github.com/safaazreqat69-gif/AI381_Lab2/actions/workflows/ci.yml)

## Overview

This project demonstrates an end-to-end MLOps workflow for serving a machine learning model through a FastAPI application.

The project includes automated testing, code linting, Docker containerization, vulnerability scanning, and automated publishing of the Docker image to GitHub Container Registry (GHCR).

## Project Structure

```text
AI381_Lab2/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
├── tests/
├── Dockerfile
├── requirements.txt
├── model.joblib
└── README.md
```

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Docker
- GitHub Actions
- Ruff
- Pytest
- Trivy
- GitHub Container Registry (GHCR)

## Features

- Machine learning model serving through a FastAPI application.
- Health-check endpoint for application availability.
- Automated testing with Pytest.
- Code quality checks with Ruff.
- Multi-stage Docker image build.
- Non-root user for running the application container.
- Docker health check.
- Container vulnerability scanning with Trivy.
- Automated CI/CD workflow using GitHub Actions.
- Docker image publishing to GHCR after successful checks.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/safaazreqat69-gif/AI381_Lab2.git
cd AI381_Lab2
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

The API should be available at:

- Health check: `http://localhost:8000/health`
- API documentation: `http://localhost:8000/docs`

## Run Tests

```bash
python -m pytest tests/ -v
```

## Run Code Quality Checks

```bash
python -m ruff check src/ tests/
```

## Run with Docker

Build the Docker image:

```bash
docker build -t ai381-lab2:latest .
```

Run the container:

```bash
docker run --rm -p 8000:8000 ai381-lab2:latest
```

Check the health endpoint:

```text
http://localhost:8000/health
```

## CI/CD Pipeline

The GitHub Actions workflow runs on pushes to `main` and pull requests targeting `main`.

The workflow performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs Ruff linting.
5. Executes automated tests.
6. Builds the Docker image.
7. Scans the image with Trivy for CRITICAL and HIGH vulnerabilities.
8. Publishes the image to GHCR after the required checks succeed.

## Container Registry

The Docker image is published to GitHub Container Registry.

Repository:

https://github.com/safaazreqat69-gif/AI381_Lab2

## Academic Context

Course: AI381 — MLOps

Lab: Lab 2

This project demonstrates practical MLOps concepts, including model serving, automated testing, containerization, continuous integration, security scanning, and container image publishing.
