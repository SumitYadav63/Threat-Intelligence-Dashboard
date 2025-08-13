import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")
BASE_URL = "https://otx.alienvault.com/api/v1"
headers = {"X-OTX-API-KEY": API_KEY}

# Fetch pulses
def fetch_pulses():
    response = requests.get(f"{BASE_URL}/pulses/subscribed", headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Save to CSV
def save_to_csv(pulses, filename="pulses.csv"):
    df = pd.DataFrame(pulses)
    df.to_csv(filename, index=False)
    print(f"Saved {len(pulses)} pulses to {filename}")

if __name__ == "__main__":
    pulses = fetch_pulses()
    if pulses:
        save_to_csv(pulses)