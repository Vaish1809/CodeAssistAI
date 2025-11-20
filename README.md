# CodeAssist AI – Developer Productivity Tool

**CodeAssist AI** is a full-stack serverless application designed to boost developer productivity. It features an AI-powered backend that generates code stubs and provides debugging insights, deployed on AWS Lambda for scalability.

## 🏗 Architecture

1.  **Frontend**: React.js (Single Page Application) for code editing and interaction.
2.  **Backend**: FastAPI (Python) wrapped with **Mangum** for AWS Lambda compatibility.
3.  **Database**: PostgreSQL for storing user snippets and audit logs.
4.  **AI Engine**: OpenAI API (GPT-4/3.5) for code generation and analysis.
5.  **DevOps**: Docker Compose for local dev, GitHub Actions for CI/CD.

## 🚀 Tech Stack

* **Python 3.10** / **FastAPI**
* **React.js 18**
* **PostgreSQL 15**
* **AWS Lambda** (Serverless)
* **Docker & Docker Compose**

## 🛠 How to Run Locally

1.  **Prerequisites**: Docker Desktop installed.
2.  **Setup Environment**:
    Create a `.env` file in `backend/` (optional, defaults provided in code):
    ```
    DATABASE_URL=postgresql://user:password@db:5432/codeassist
    OPENAI_API_KEY=your_key_here  # Leave empty to use Mock Mode
    ```
3.  **Build and Run**:
    ```bash
    docker-compose up --build
    ```
4.  **Access**:
    * **Frontend**: http://localhost:3000
    * **Backend Docs**: http://localhost:8000/docs

## ☁️ AWS Lambda Deployment Strategy
The backend utilizes `Mangum` to wrap the FastAPI app. In a real deployment:
1.  The Docker container is pushed to **AWS ECR**.
2.  **AWS Lambda** is configured to run the container image.
3.  **API Gateway** routes requests to the Lambda function.