FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl ffmpeg espeak

COPY . .

EXPOSE 80

CMD ["python3", "main.py"]