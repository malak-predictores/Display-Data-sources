# 📊 Data Transparency Chat Interface

This project aims to increase transparency and user trust in data-driven insights by **clearly displaying the data source for each data point**. The chat-based interface allows users to query insights, while all returned data includes its source—such as from [data.europa.eu](https://data.europa.eu), [IMF](https://www.imf.org/external/datamapper/api/), or [opendata.swiss](https://opendata.swiss/en/).



---

## ⚙️ Tech Stack

| Layer     | Tech                            |
|-----------|---------------------------------|
| Backend   | FastAPI (Python)                |
| Frontend  | React + TypeScript              |
| Caching   | Redis                           |
| Data APIs | IMF, data.europa.eu, opendata.swiss |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js + npm
- Redis server installed and running locally on port `6379`


---

## 🛠 Tech Stack

- 🔙 **Backend**: Python + FastAPI
- 🔧 **Cache**: Redis
- 🌐 **Frontend**: React + TypeScript
- 📡 **Data Sources**:
  - [data.europa.eu](https://data.europa.eu/en/about/documentation)
  - [IMF Data Mapper API](https://www.imf.org/external/datamapper/api/)
  - [opendata.swiss](https://opendata.swiss/en/)

---


### 1. Redis (local)

Install and run Redis:


sudo apt install redis
sudo systemctl start redis

---

### 2. Backend Setup (FastAPI)

cd backend

python3 -m venv venv11

source venv11/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

---
### 3. Frontend Setup (React)

cd frontend

npm install

npm start


