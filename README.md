# Retail-Customer-Behavior-Analysis
# Retail Customer Behavior Analysis

A customer segmentation analysis project that uses machine learning to identify distinct customer groups based on their spending patterns and annual income.

## Project Overview

This project analyzes customer behavior data from a retail mall to discover meaningful customer segments using K-means clustering. The analysis includes data visualization and elbow method optimization to determine the optimal number of customer clusters.

## Features

- **Data Exploration**: Summary statistics and data information
- **Visualizations**: 
  - Customer age distribution histogram
  - Income vs spending score scatter plot
  - Elbow curve for cluster optimization
  - Final cluster visualization
- **Machine Learning**: K-means clustering for customer segmentation
- **Feature Scaling**: StandardScaler preprocessing for normalized features

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

## Installation

Install required dependencies:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Usage

Run the analysis script:
```bash
python analysis.py
```

The script will:
1. Load customer data from `Mall_Customers.csv`
2. Display initial data exploration (head, info, describe)
3. Generate visualizations of age distribution and spending patterns
4. Perform K-means clustering with elbow method analysis
5. Display cluster visualizations

## Data

The analysis uses `Mall_Customers.csv` which contains:
- **CustomerID**: Unique customer identifier
- **Gender**: Customer gender
- **Age**: Customer age
- **Annual Income (k$)**: Annual income in thousands
- **Spending Score (1-100)**: Customer spending score

## Project Files

- `analysis.py` - Main analysis script
- `Mall_Customers.csv` - Customer dataset
- `README.md` - Project documentation
- `API_DOCS.md` - Additional API documentation

## Output
<img width="1845" height="956" alt="Screenshot 2026-06-05 112533" src="https://github.com/user-attachments/assets/bd9b5199-23ae-4488-ac45-4aadb15ab786" />

<img width="1842" height="931" alt="Screenshot 2026-06-05 112545" src="https://github.com/user-attachments/assets/496dbf77-f0dc-4dd6-a016-961e28aaf8b5" />



The analysis generates several visualizations using matplotlib/seaborn that appear in separate windows:
- Age distribution plot
- Income vs spending scatter plot
- Elbow curve for optimal cluster selection
- Final customer segments visualization

## Author

Samadhan Trambak Shinde
