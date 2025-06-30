# 🐧 Penguin Analyzer

A simple, object-oriented Python project using the Seaborn Penguins dataset to explore and analyze penguin data.

This project includes:
- 📊 Data analysis with Pandas
- 🧪 Unit testing with Pytest
- 🎨 Interactive visualization using Streamlit
- 📦 Clean Python project structure

## Project Structure

penguin_analyzer/
├── penguin_analyzer/
│ ├── init.py
│ ├── data_loader.py
│ └── analyzer.py
├── tests/
│ └── test_penguin_analyzer.py
├── app.py ← Streamlit dashboard
├── main.py ← Script to run basic analysis
├── requirements.txt
├── README.md
└── .gitignore

### Streamlit Dashboard
This dashboard lets you:
- View penguin species counts
- Calculate average body mass
- Filter by species
- Generate Seaborn pairplots interactively
