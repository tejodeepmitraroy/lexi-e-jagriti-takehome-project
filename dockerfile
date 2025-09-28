FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Start FastAPI with uvicorn
CMD ["uvicorn", "src.main:app", "--reload"]
