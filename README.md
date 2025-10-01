# 🥛 Milk Price Prediction Project

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Nixtla](https://img.shields.io/badge/Powered%20by-Nixtla-orange.svg)](https://nixtla.github.io/mlforecast/)

> Predicting farmgate milk prices in Brazil using machine learning and time series forecasting techniques.

## 📊 Project Overview

This project focuses on predicting the **farmgate milk price** (`price_to_producer`) for Brazilian milk manufacturers with a forecasting horizon of **one year**. The challenge combines time series analysis with regression modeling to understand the complex dynamics affecting milk pricing in the Brazilian market.

### 🎯 Problem Statement

Milk price prediction is crucial for:
- **Farmers** 📈 Planning production and investment decisions
- **Manufacturers** 🏭 Supply chain optimization and cost management  
- **Policy Makers** 🏛️ Market regulation and agricultural policy development
- **Investors** 💰 Risk assessment in the dairy industry

## 📁 Project Structure

```
milk-prediction/
│
├── 📊 data/
│   ├── Desafio_Inteligência de Dados_MilkPoint.xlsx  # Raw data file
│   └── tidy_data.csv                                 # Cleaned dataset
│
├── 📓 notebooks/
│   ├── 01-EDA.ipynb           # 🔍 Exploratory Data Analysis
│   ├── 02-Regression.ipynb    # 📈 Statistical regression models
│   ├── 03-ML.ipynb           # 🤖 Machine learning approaches
│   └── 05-all-in-one.ipynb  # 🎯 Complete pipeline
│
├── 📋 main.py                # Main execution script
├── 📦 pyproject.toml         # Project dependencies
├── 🔒 uv.lock               # Dependency lock file
└── 📖 README.md             # Project documentation
```

## 📈 Dataset & Features

The dataset contains monthly time series data with the following indicators:

### 🔸 Supply Indicators
- **Milk Production** 🥛 Monthly milk output volumes
- **Imports/Exports** 🌍 International trade flows
- **Total Supply** 📦 Overall market availability
- **Per Capita Supply** 👥 Supply per person metrics

### 🔸 Demand Indicators  
- **UHT Milk Industry** 🏭 Industrial demand metrics
- **UHT Milk Market** 🛒 Consumer market demand
- **Unemployment Rate** 📊 Economic indicators
- **Wage Mass** 💵 Purchasing power metrics
- **Population** 👫 Demographic factors

### 🎯 Target Variable
- **Farmgate Milk Price** 💰 Price paid to producers (target for prediction)

## 🧠 Methodology

### 1. 🔍 Exploratory Data Analysis (EDA)
- **Correlation Analysis** 📊 Understanding relationships between variables
- **Trend & Seasonality** 📈 Identifying temporal patterns
- **Missing Data Assessment** ❓ Data quality evaluation
- **Supply vs Demand Dynamics** ⚖️ Market behavior analysis

### 2. 📈 Regression Modeling
- **Linear Regression** 📏 Baseline statistical model using OLS
- **Feature Engineering** 🔧 Creating relevant predictors
- **Cross-validation** ✅ Model validation with last 12 months
- **Performance Metrics** 📊 RMSE, MAE, MAPE evaluation

### 3. 🤖 Machine Learning Approaches
Multiple algorithms were tested and compared:
- **Linear Regression** 📏 Baseline model
- **Random Forest** 🌳 Ensemble method
- **Huber Regressor** 🎯 Robust regression
- **Bayesian Ridge** 🧮 Final selected model

### 4. 🔮 Covariate Forecasting
Each predictor variable was modeled separately to create future predictions:
- **Individual time series models** for each covariate
- **Univariate forecasting** approach
- **Feature-specific modeling** to capture unique patterns

## 🏆 Final Model Selection

After extensive experimentation and evaluation, the **Bayesian Ridge Regression** was selected as the final model due to:

- ✅ **Superior predictive performance** on validation data
- ✅ **Robust handling of multicollinearity** among features  
- ✅ **Uncertainty quantification** through Bayesian approach
- ✅ **Regularization benefits** preventing overfitting

## 🛠️ Tools & Technologies

### Core Libraries
- **Nixtla MLForecast** 🚀 Primary forecasting framework
- **Pandas** 🐼 Data manipulation and analysis
- **NumPy** 🔢 Numerical computing
- **Scikit-learn** 🧠 Machine learning algorithms

### Visualization & Analysis  
- **Plotnine** 📊 Grammar of graphics (ggplot2 style)
- **Matplotlib** 📈 Statistical plotting
- **Seaborn** 🎨 Statistical data visualization

### Statistical Modeling
- **Statsmodels** 📊 Statistical analysis and regression
- **UtilsForecast** ⚡ Evaluation and utility functions

## 📊 Results & Performance

The final Bayesian Ridge model achieved:
- **Low prediction bias** 📉 Minimal systematic errors
- **Competitive RMSE** 🎯 Strong accuracy on validation set
- **Robust generalization** ✅ Consistent performance across time periods

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Heitorcp/milk-price-prediction.git
cd milk-price-prediction
```

2. **Install dependencies**
```bash
uv sync
```

3. **Activate virtual environment**
```bash
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

4. **Run the analysis**
```bash
python main.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

**Heitor** - [@Heitorcp](https://github.com/Heitorcp)

---
*Made with ❤️ for the Brazilian dairy industry*
