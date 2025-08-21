FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt
RUN pip install -r requirements.txt

COPY core/ ./core/
COPY infrastructure/ ./infrastructure/
COPY main.py .

CMD ["python", "main.py"]