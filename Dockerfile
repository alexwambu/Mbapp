# ---- Stage 1: Builder ----
FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install -y curl jq && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# If only static_index.html exists, create static/index.html automatically
RUN mkdir -p /app/static && \
    if [ -f /app/static_index.html ] && [ ! -f /app/static/index.html ]; then \
        mv /app/static_index.html /app/static/index.html; \
    fi

# ---- Stage 2: Runtime ----
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
