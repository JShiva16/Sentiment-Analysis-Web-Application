# 📱 Mobile Reviews Sentiment Analysis System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> A Python-based NLP system that analyzes customer reviews of mobile products and classifies
> sentiment as **Positive**, **Negative**, or **Neutral** — with an interactive web interface
> to explore and compare models in real time.


## ✨ Features

- 🏢 **Company & Model Filter** — Browse reviews by selecting a specific brand and phone model
- ⚖️ **Side-by-Side Comparison** — Compare sentiment scores of two different mobile models at once
- 😊 **Sentiment Classification** — Classifies reviews as Positive, Negative, or Neutral using NLP
- 📊 **Visual Insights** — Sentiment distribution charts for quick understanding
- 🌐 **Clean Web Interface** — Simple two-page UI: Explorer page + Comparison page
- 📓 **Jupyter Notebook** — Full EDA, preprocessing pipeline, and model evaluation included

---

## 📁 Project Structure
```
mobile-reviews-sentiment/
│
├── main.py                          # Entry point — runs the Flask web app
├── requirements.txt                 # All Python dependencies
├── sentiment_analysis.ipynb         # Jupyter Notebook for EDA & model building
│
├── data/
│   └── dataset.csv         # Labelled mobile reviews dataset
│
├── static/
│   ├── compare.js                   # JS logic for the Compare Models page
│   ├── script.js                    # JS logic for the Explorer page
│   └── style.css                    # Stylesheet for the web interface
│
└── templates/
    ├── index.html                   # Main page — Mobile Reviews Explorer
    └── .html                 # Compare Models page
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| NLP | NLTK / TextBlob / scikit-learn |
| Web Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Notebook | Jupyter |

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/JShiva16/mobile-reviews-sentiment.git
   cd mobile-reviews-sentiment
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Download NLTK data** *(if applicable)*
```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
```

4. **Run the application**
```bash
   python main.py
```

5. **Open in browser**
```
   http://localhost:5000
```

---

## 💡 Usage

### 🔎 Reviews Explorer (index page)
1. Select a **Company** from the dropdown (e.g., Samsung, Apple, OnePlus)
2. Select a **Model** (filtered by company)
3. Click **Show Reviews** to display sentiment analysis results
4. Click **Comparison Models** to navigate to the comparison page

### ⚖️ Compare Models Page
1. Select **Company 1** and its **Model**
2. Select **Company 2** and its **Model**
3. Click **Show Comparison** to view a side-by-side sentiment breakdown
4. Use the **← Back** link to return to the Explorer

### 📓 Jupyter Notebook
```bash
jupyter notebook sentiment_analysis.ipynb
```

---

## 📂 Dataset

The dataset (`dataset.csv`) contains mobile product reviews:

| Column | Description |
|---|---|
| `review` | Raw customer review text |
| `sentiment` | Label: Positive / Negative / Neutral |
| `product` | Mobile model name |
| `company` | Brand/manufacturer |
| `rating` | Star rating (1–5) |

## 🤝 Contributing

1. Fork the project
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub:https://github.com/JShiva16
- LinkedIn:https://linkedin.com/in/jinkashiva

---

⭐ **Star this repo if you found it useful!**
