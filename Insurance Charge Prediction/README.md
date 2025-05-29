# HealthyLife Insurance Charge Prediction


## Project Overview

HealthyLife is a leading insurance provider based in New York City, offering a broad range of health, auto, and life insurance products across the U.S. 
The company currently uses conventional techniques to estimate insurance charges, which often result in inaccurate pricing due to limited understanding 
of how customer attributes influence premiums.

This project aims to enhance HealthyLife's pricing strategy by building a predictive model and deploying an app that estimates health insurance charges 
using customer data such as age, sex, BMI, smoking habits, and region.


## Objective
- Develop a robust **predictive model** to estimate insurance charges based on individual attributes.
- Build an **interactive Gradio application** to streamline the underwriting and pricing process.
- Ensure **regulatory compliance** and improve **pricing transparency**.
- Monitor and analyze **model/data drift** to ensure consistent and reliable performance over time.


## Key Outcomes

By implementing this solution, HealthyLife aims to:

- Provide **accurate and personalized premium estimates**.
- Minimize risks associated with **underpricing or overpricing**.
- Increase **customer satisfaction and loyalty**.
- Maintain **regulatory compliance** in all pricing decisions.
- Enhance **competitiveness and profitability** in the insurance market.


## Tech Stack

- **Language**: Python  
- **Libraries**: scikit-learn, pandas, numpy, matplotlib, seaborn  
- **App Framework**: Gradio (for UI deployment)  
- **Model Monitoring & Experiment Tracking**: MLflow  
- **Version Control**: Git & GitHub


##  Dataset

The dataset includes the following fields:
- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`
- `charges` (target variable)

*Note: This dataset may be synthetic or anonymized for privacy.*


## Features

- Exploratory Data Analysis (EDA) to understand attribute influence.
- Regression model to predict insurance charges.
- Model evaluation using R², MAE, and RMSE.
- **MLflow integration** for model tracking, versioning, and comparison.
- Gradio-based web app for real-time charge estimation.


##  How to Run

1. Clone the repository  
   `git clone https://github.com/yourusername/healthylife-insurance-predictor.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the Gradio app  
   `python app.py`

4. Start MLflow tracking UI (optional)  
   `mlflow ui`




