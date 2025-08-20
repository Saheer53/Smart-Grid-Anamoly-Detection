# Smart Grid Anomaly Detection

This project focuses on developing an anomaly detection system for smart grid networks using advanced machine learning techniques. It leverages the Industrial Control Systems (ICS) dataset to identify potential cyberattacks and irregular patterns, enhancing the reliability and security of smart grids. 

# Overview

Smart grids integrate digital communication technologies with traditional power grids, increasing efficiency and sustainability but also exposing them to cyber threats such as DoS attacks, command injections, and unauthorized access.
Our goal was to build a robust anomaly detection framework capable of real-time monitoring and security enhancement.

# Methodology
# Data Preparation

Dataset: ICS dataset (covering normal operations + simulated cyberattacks)

Cleaning: handled inconsistencies, missing values, and duplicate records

Standardization: scaled numeric features (srcPort, dstPort, ipLen) using StandardScaler

Encoding: categorical values (e.g., IP addresses) converted via one-hot encoding 

# Exploratory Data Analysis (EDA)

Histograms & boxplots revealed outliers (notably in ipLen and Relative Time)

Correlation matrix identified strong relationships (e.g., ipLen and Relative Time)

Scatter plots & pairplots visualized separation between normal and anomalous data 

# Feature Engineering & Selection

Feature importance evaluation using Random Forest

Dimensionality reduction with Principal Component Analysis (PCA) (retaining 95% variance)

Key features identified: Relative Time, TimeStamp_sec, ipLen, dstPort, srcPort 

# Models Explored

Isolation Forest – effective for high-dimensional anomalies

Autoencoders – used reconstruction error to detect subtle anomalies

One-Class SVM – defined decision boundaries for anomalies

KNN, XGBoost, LOF, Ridge Regression also tested 

# Final Model

Stacked Classifier Model with parallel processing

Combined strengths of multiple algorithms

Delivered balanced precision & recall and robust real-time detection performance 

# Results

Best Performing Model: Stacked Classifier

Evaluation Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC

Prediction Distribution: ~80% normal vs ~20% anomalies on unseen data

Deployment-ready with high accuracy in distinguishing threats vs normal operations 

# Deployment

Implemented a Flask API for real-time anomaly detection

Endpoint /predict accepts smart grid data in JSON, returns classification (normal or anomaly)

API tested locally; scalable for cloud deployment or integration with grid infrastructure 

# Project Structure
SmartGrid-Anomaly-Detection/
├─ data/                  # ICS dataset (not included in repo)
├─ notebooks/             # EDA and experimentation
├─ preprocessing/         # data cleaning, normalization, encoding
├─ models/                # saved models (stacked classifier, PCA, preprocessor)
├─ app.py                 # Flask API for deployment
├─ requirements.txt
└─ README.md

# Requirements
pandas
numpy
scikit-learn
matplotlib
seaborn
flask
xgboost

# Future Work

Extend to other anomaly detection models (deep learning, graph-based methods)

More feature engineering for cyber-attack patterns

Cloud-native deployment for real-time monitoring at scale

Integration with broader smart grid security frameworks 

# References

ICS Dataset for Smart Grid Anomaly Detection: IEEE Dataport 

Olson, D.L., & Delen, D. Advanced Data Mining Techniques, 2008.
