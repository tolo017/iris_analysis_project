# Iris Flower Dataset Analysis

![Iris Flowers](outputs/figures/sepal_length_comparison.png)

## Project Overview

This project analyzes the classic Iris flower dataset, containing measurements of three Iris species. The analysis includes:

- Data loading and cleaning
- Exploratory data analysis
- Statistical summaries
- Data visualization

## Project Structure
iris_analysis_project/
├── data/ # Raw data files
├── notebooks/ # Jupyter notebooks
├── scripts/ # Python modules
├── outputs/ # Generated outputs
│ ├── figures/ # Visualization images
│ └── reports/ # Analysis reports
├── .gitignore # Files to ignore in version control
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-analysis.git
   cd iris-analysis

python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

pip install -r requirements.txt

# Run
python scripts/data_loading.py


# Launch Jupyter Notebook
jupyter notebook notebooks/analysis.ipynb