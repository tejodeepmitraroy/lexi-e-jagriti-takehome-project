FROM Python

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Install playwright browsers
RUN playwright install --with-deps
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]