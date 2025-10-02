# ---- Stage 1: Builder ----
FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: Runtime ----
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app files
COPY server.py .
COPY entrypoint.sh .
COPY static ./static

RUN chmod +x /app/entrypoint.sh

# Create persistent storage dir
RUN mkdir -p /data

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
