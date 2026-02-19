<div align="center">

<!-- HEADER BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Stock%20Prediction%20LLM&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=AI-Powered%20Stock%20Forecasting%20with%20Google%20Gemini&descAlignY=55&descSize=18"/>

<!-- BADGES ROW 1 -->
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<!-- BADGES ROW 2 -->
[![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-API-6001D2?style=for-the-badge&logo=yahoo&logoColor=white)](https://finance.yahoo.com)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)



<br/>

> **⚡ A hybrid AI-driven stock prediction system combining real-time Yahoo Finance data with Google Gemini LLM — wrapped in a clean Streamlit interface.**

</div>

---

## 🚀 Overview

**Stock Prediction LLM** is an intelligent forecasting system that fetches live market data from **Yahoo Finance**, processes it with **Pandas & NumPy**, and enhances predictions using **Google Gemini AI** — all surfaced through an interactive **Streamlit** web dashboard.

It's designed to be beginner-friendly yet powerful enough for serious analysis, with built-in evaluation metrics and rich visual trend charts.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📡 **Real-time Data** | Live stock prices from Yahoo Finance API |
| 🤖 **Gemini AI Engine** | LLM-enhanced intelligent price prediction |
| 📊 **Interactive Charts** | Matplotlib-powered historical & forecast visuals |
| 📈 **Performance Metrics** | MAE, RMSE, R² evaluation out of the box |
| 🖥️ **Clean UI** | No-friction Streamlit web interface |
| 🔣 **Any Stock Symbol** | Just type a ticker — system handles the rest |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────┐
│           User Input (Stock Symbol)         │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│           Yahoo Finance API                 │
│         (Real-time Market Data)             │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│       Data Preprocessing Layer              │
│           Pandas  ·  NumPy                  │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│  ★  Prediction Engine  ★                   │
│   Baseline Model  +  Google Gemini LLM      │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│         Visualization (Matplotlib)          │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│        Streamlit Web Interface              │
│   (Charts · Metrics · Predictions UI)      │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology | Badge |
|---|---|---|
| **Language** | Python 3.10+ | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Frontend** | Streamlit | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **Data Handling** | Pandas, NumPy | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) |
| **AI / ML** | Google Gemini API | ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=google&logoColor=white) |
| **Visualization** | Matplotlib | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) |
| **Data Source** | Yahoo Finance | ![Yahoo](https://img.shields.io/badge/Yahoo%20Finance-6001D2?style=flat-square&logo=yahoo&logoColor=white) |
| **Environment** | VS Code | ![VSCode](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) |
| **Version Control** | Git + GitHub | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) |

</div>

---

## 📊 Performance Metrics

<div align="center">

| Metric | Full Name | Purpose |
|:---:|---|---|
| ![MAE](https://img.shields.io/badge/MAE-Mean%20Absolute%20Error-22c55e?style=flat-square) | Mean Absolute Error | Average magnitude of prediction error |
| ![RMSE](https://img.shields.io/badge/RMSE-Root%20Mean%20Square%20Error-f59e0b?style=flat-square) | Root Mean Square Error | Penalizes larger deviations more heavily |
| ![R²](https://img.shields.io/badge/R²-R--Squared%20Score-60a5fa?style=flat-square) | R-Squared Score | Goodness-of-fit for the prediction model |

</div>

---

## ⚙️ Installation & Setup

### Prerequisites

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![pip](https://img.shields.io/badge/pip-latest-3776AB?style=flat-square&logo=pypi&logoColor=white)
![Gemini Key](https://img.shields.io/badge/Gemini-API%20Key%20Required-8E75B2?style=flat-square&logo=google&logoColor=white)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/stock-prediction-llm.git
cd stock-prediction-llm
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **requirements.txt** includes: `streamlit`, `yfinance`, `pandas`, `numpy`, `matplotlib`, `google-generativeai`, `python-dotenv`, `scikit-learn`

### Step 3 — Configure Environment

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> 🔑 Get your free Gemini API key at [ai.google.dev](https://ai.google.dev)

### Step 4 — Run the Application

```bash
streamlit run app.py
```

Then open **http://localhost:8501** in your browser. 🎉

---

## 📁 Project Structure

```
stock-prediction-llm/
│
├── app.py                  # Main Streamlit application
├── accuracy.py            # shows accuracy
├       
├       
├            
│
├── .env                    # API keys (DO NOT commit)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🌟 Screenshots

> 📸 Add your Streamlit app screenshots below

```
[ Screenshot Placeholder — Run the app and add screenshots here ]
```

---

## 🔮 Roadmap

- [x] Real-time Yahoo Finance data fetching
- [x] Gemini LLM prediction integration
- [x] MAE / RMSE / R² evaluation
- [x] Interactive Streamlit UI
- [ ] LSTM & Deep Learning integration
- [ ] Real-time streaming price updates
- [ ] Multiple technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Cloud deployment (AWS / GCP)
- [ ] Multi-user authentication & security

---

## 🤝 Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-22c55e?style=for-the-badge&logo=github)](https://github.com/your-username/stock-prediction-llm/pulls)

Contributions, issues, and feature requests are welcome!

1. **Fork** the repository
2. Create a feature branch — `git checkout -b feature/your-feature`
3. Commit changes — `git commit -m "feat: add your feature"`
4. Push to branch — `git push origin feature/your-feature`
5. Open a **Pull Request**

---

## 👨‍💻 Author

<div align="center">

**Ranit Shaw**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your@email.com)

B.Tech — Computer Science & Engineering
**University of Engineering & Management, Jaipur**

</div>

---

## ⭐ Support

If this project helped you, please consider:

[![Star](https://img.shields.io/badge/⭐%20Star%20this%20Repo-fbbf24?style=for-the-badge&logo=github&logoColor=black)](https://github.com/your-username/stock-prediction-llm)
[![Fork](https://img.shields.io/badge/🍴%20Fork%20it-60a5fa?style=for-the-badge&logo=github&logoColor=black)](https://github.com/your-username/stock-prediction-llm/fork)
[![Share](https://img.shields.io/badge/📢%20Share-f472b6?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/intent/tweet?text=Check%20out%20this%20AI%20Stock%20Prediction%20system!%20https://github.com/your-username/stock-prediction-llm)

---

## 📄 License

[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>

**Made with ❤️ by Ranit Shaw**

</div>
