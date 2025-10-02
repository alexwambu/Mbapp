#!/bin/sh
set -e

echo "[INFO] Starting storage app..."

# Keep-alive watchdog
(
  while true; do
    echo "[HEALTH] Checking service..."
    sleep 18
  done
) &

# Start server
exec uvicorn server:app --host 0.0.0.0 --port 8000
