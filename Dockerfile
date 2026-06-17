# Start from a small, official Python image (slim = lightweight).
FROM python:3.13-slim

# All following commands run inside /app in the container.
WORKDIR /app

# Install dependencies first so Docker can cache this layer
# (it only re-runs if requirements.txt changes, not on every code edit).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the analysis script and the data into the image.
COPY detect_anomalies.py .
COPY telemetry_data.csv .

# Run the anomaly detection when the container starts.
CMD ["python", "detect_anomalies.py", "telemetry_data.csv"]
