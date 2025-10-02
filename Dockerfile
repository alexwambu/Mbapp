# ---- Stage 1: Builder ----
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: Runtime ----
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# Copy source code
COPY . .

# Make static folder available
RUN mkdir -p /app/static

EXPOSE 8000
CMD ["python", "server.py"]
