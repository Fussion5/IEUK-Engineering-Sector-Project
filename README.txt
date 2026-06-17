========================================
  AeroGrid Turbine Anomaly Detector
  IEUK 2026 Engineering Project
  W. Dominic Fernando
  dominicfernando74@gmail.com
========================================

WHAT THIS DOES
--------------
This tool reads sensor data from offshore wind turbines and automatically
identifies which turbines need urgent maintenance. It flags turbines if:
  - Their average temperature exceeds 85°C (overheating), OR
  - Their vibration spikes above 15.0 mm/s (mechanical fault)

The results from the included data show:
  - T-04: overheating (avg temp 90.6°C)
  - T-07: excessive vibration (25.0 mm/s)
  - All other 8 turbines: healthy


HOW TO RUN IT — OPTION A: Python (simpler)
------------------------------------------
Use this if you already have Python installed on your computer.

Step 1 — Open a terminal (PowerShell on Windows, Terminal on Mac).

Step 2 — Navigate to this folder. For example:
    cd C:\Users\YourName\Downloads\<ThisFolder>

Step 3 — Install the required library (only needed once):
    pip install pandas

Step 4 — Run the script:
    python detect_anomalies.py telemetry_data.csv

You should see output like:
    Failing turbines (urgent maintenance required):
      - T-04: avg temp 90.6C > 85.0C
      - T-07: max vibration 25.0 mm/s > 15.0 mm/s


HOW TO RUN IT — OPTION B: Docker (no Python needed)
----------------------------------------------------
Use this if you don't have Python, or want a clean isolated environment.
You'll need Docker Desktop installed (free download from docker.com).

Step 1 — Make sure Docker Desktop is open and running.

Step 2 — Open a terminal and navigate to this folder:
    cd C:\Users\YourName\Downloads\<ThisFolder>

Step 3 — Build the Docker image (only needed once):
    "docker build -t aerogrid-anomaly ."

    Note: the dot at the end is important - don't leave it out.

Step 4 — Run it:
    "docker run --rm aerogrid-anomaly"

You should see the same output as Option A above.


TROUBLESHOOTING
---------------
"docker-credential-desktop not found" error when building:
    1. Open the file: C:\Users\<YourName>\.docker\config.json
    2. Change  "credsStore": "desktop"  to  "credsStore": ""
    3. Save the file and try again.

"python not found" or "pip not found":
    Python is not installed. Download it from python.org and
    make sure to tick "Add Python to PATH" during installation.

"No module named pandas":
    Run:  pip install pandas and try again.


FILES IN THIS PROJECT
---------------------
detect_anomalies.py   - the main Python script that finds failing turbines
telemetry_data.csv    - sensor readings from 10 turbines
Dockerfile            - instructions for building the Docker container
requirements.txt      - list of Python libraries the script needs
README.txt            - this file
