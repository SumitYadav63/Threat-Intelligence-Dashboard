
# 🛡️ Threat Intelligence Dashboard — Matrix Edition

![Cyber Banner](https://i.imgur.com/9b3F4oU.png)

> **Interactive cybersecurity dashboard** that fetches real-time threat intelligence from the **AlienVault OTX API**, processes indicators (IPs, domains, file hashes), and visualizes patterns for threat hunting and SOC (Security Operations Center) workflows.

---

## 📌 Features

- **🔍 Real-Time Data** — Fetches live threat intelligence from AlienVault OTX.
- **📊 Interactive Visualizations** — Plotly-powered charts for trend analysis.
- **🛠 Advanced Filtering** — Search by pulse name or author to drill into data.
- **🎯 SOC-Ready Insights** — Identifies top contributors & recent threat surges.
- **💻 Cybersecurity UI** — Matrix-style dark theme for an immersive experience.

---

## 🗂 Tech Stack

| Layer         | Technology |
|---------------|------------|
| Backend       | Python 3, Requests |
| Frontend      | Streamlit, Plotly |
| API Source    | AlienVault OTX |
| Styling       | Custom CSS (Matrix theme) |
| Data Storage  | CSV |

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/Threat-Intelligence-Dashboard.git
   cd Threat-Intelligence-Dashboard
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the project root:

ini
Copy code
OTX_API_KEY=your_api_key_here
🚀 Usage
Fetch the latest threat pulses

bash
Copy code
python fetch_otx_data.py
Run the dashboard

bash
Copy code
streamlit run dashboard.py
Open the local URL provided by Streamlit in your browser.

📊 Example Dashboard

🌐 Live Demo
Deploy your dashboard online for free via Streamlit Cloud:

bash
Copy code
streamlit deploy
Or visit: Streamlit Cloud

🎯 Ideal Use Cases
Security Analysts monitoring latest threats.

SOC teams for quick situational awareness.

Threat Hunters researching malware campaigns.

Cybersecurity students building a portfolio project.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

📜 License
MIT License © 2025

📧 Contact
Sumit Yadav
📩 Email: worksumit02@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/sumit-yadav
🛠 GitHub: github.com/SumitYadav63