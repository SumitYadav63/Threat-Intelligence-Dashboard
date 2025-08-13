import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")
BASE_URL = "https://otx.alienvault.com/api/v1"

# Example: Get pulses (collections of threat intel)
headers = {"X-OTX-API-KEY": API_KEY}
response = requests.get(f"{BASE_URL}/pulses/subscribed", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Fetched {len(data.get('results', []))} pulses.")
    for pulse in data.get("results", [])[:5]:  # show first 5 pulses
        print(f"- {pulse['name']} (created: {pulse['created']})")
else:
    print(f"Error: {response.status_code} - {response.text}")