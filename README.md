# 🏛️ e-Jagriti API Wrapper (FastAPI)

A FastAPI-based backend that fetches and serves data from e-Jagriti
 (such as state commissions and circuit benches) through clean REST APIs.

This project helps developers easily integrate e-Jagriti state data into their own apps without worrying about scraping or API restrictions.

## 🚀 Features

Fetch all states from e-Jagriti.

Feature-based FastAPI folder structure.

Configurable via .env file.

Async & production-ready.

📂 Project Structure
app/
├── api/
│   └── v1/
│       ├── routes/
│       │   └── states.py     # States API
│       └── __init__.py
├── core/
│   ├── config.py             # Settings loader from .env
│   └── __init__.py
├── main.py                   # FastAPI entrypoint
└── __init__.py
.env
README.md

⚙️ Setup & Installation
1. Clone the Repository
git clone https://github.com/your-username/e-jagriti-fastapi.git
cd e-jagriti-fastapi

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the project root:

API_BASE_URL=https://e-jagriti.gov.in/services/report/report/getStateCommissionAndCircuitBench

▶️ Run the Server
uvicorn app.main:app --reload


Server runs at: http://127.0.0.1:8000

📡 API Documentation

FastAPI automatically generates Swagger and ReDoc docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🛠️ API Endpoints
🔹 Get All States

Endpoint:

GET /api/v1/states


Response Example:

{
  "states": [
    {
      "stateCode": "AP",
      "stateName": "Andhra Pradesh",
      "commission": "Andhra Pradesh State Commission",
      "circuitBench": null
    },
    {
      "stateCode": "WB",
      "stateName": "West Bengal",
      "commission": "West Bengal State Commission",
      "circuitBench": "Kolkata"
    }
  ]
}

🧪 Testing

Run tests (if you added pytest/unittest):

pytest

📜 License

MIT License © 2025 [Your Name]