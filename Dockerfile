FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN mkdir -p /app/uploads

ARG PORT=5000
ENV PORT=${PORT}
EXPOSE ${PORT}

# Gunicorn with dynamic port from ENV
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} app:app --workers 1 --timeout 0"]
