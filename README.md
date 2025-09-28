# 🏛️ E-Jagriti API Wrapper by Lexi - Backend Engineer Test (FastAPI)

A FastAPI-based backend that fetches and serves data from e-Jagriti
 (such as state commissions and circuit benches) through clean REST APIs.

This project helps developers easily integrate e-Jagriti state data into their own apps without worrying about scraping or API restrictions.

## 🚀 Features

- Fetch all states from e-Jagriti.

- Feature-based FastAPI folder structure.

- Configurable via .env file.

- Async & production-ready.

## 📂 Project Structure

```bash
├── requirements.txt       # Project dependencies
├── Dockerfile             # Docker build file
├── .dockerignore          # Files & folders to ignore in Docker
├── README.md              # Documentation
│
└── src/
    ├── core/
    │   ├── config.py          # Loads environment variables & settings
    │   └──model.py
    │
    ├── features/
    │   ├── states/
    │   ├── commissions/
    │   └── cases/
    │              
    └── main.py                # FastAPI app entrypoint
```

## 🚀 Running the Project Locally  

Follow these steps to run the project on your local machine:

### 1️⃣ Clone the Repository  
Clone the Repository git clone https://github.com/your-username/e-jagriti-fastapi.git cd e-jagriti-fastapi
```bash
git clone https://github.com/tejodeepmitraroy/lexi-e-jagriti-takehome-project.git
cd lexi-e-jagriti-takehome-project
```
### 2️⃣ Create a Virtual Environment
It’s recommended to use a virtual environment for dependencies.

```bash
python -m venv venv
```


Activate the virtual environment:

- On Linux/Mac:
```bash
source venv/bin/activate
```

- On Windows:
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Install the required dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```
Add your environment variables:

```bash
BASE_API_URL=https://e-jagriti.gov.in/services
```

### 5️⃣ Run the Server

```bash
uvicorn src.main:app --reload
```

Server runs at: http://127.0.0.1:8000

### 6️⃣ API Documentation

FastAPI automatically generates Swagger and ReDoc docs:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc


## 🐳 Running the Project with Docker

If you prefer running with Docker, follow these steps:

### 1️⃣ Build the Docker Image
```
docker build -t e-jagriti-backend .
```
### 2️⃣ Run the Container
```
docker run -d -p 8000:8000 --env-file .env e-jagriti-backend
```

### 3️⃣ Access the API

After the container starts, you can access the API at:

Swagger Docs → http://localhost:8000/docs

Redoc Docs → http://localhost:8000/redoc


📜 License

MIT License © 2025, Tejodeep Mitra Roy