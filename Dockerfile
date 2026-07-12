FROM python:3.11-slim AS builder

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --target /install fastapi uvicorn

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local/lib/python3.11/site-packages/
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
