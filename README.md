# Iris Flower Prediction - End-to-End ML App

## Project Overview

This project is an end-to-end Machine Learning system that predicts the species of an Iris flower based on its features (sepal length, sepal width, petal length, petal width). The system includes:

- Model training using the Iris dataset
- Backend API with FastAPI exposing a `/predict` endpoint
- Frontend user interface built with Streamlit
- Experiment tracking with MLflow
- Deployment on Render (backend) and Streamlit Cloud (frontend)

---

## Project Structure

ml_app_assignment/
├── ml/
│ ├── training.ipynb # Jupyter notebook for model training & preprocessing
│ └── model.pkl # Trained and saved ML model
├── backend/
│ └── main.py # FastAPI backend app
├── frontend/
│ └── streamlit_app.py # Streamlit frontend app
├── mlflow_tracking/
│ └── tracking_setup.md # MLflow setup details and screenshots
├── Dockerfile (optional) # Dockerfile for containerization (if created)
├── requirements.txt # Python dependencies
└── README.md # This file

## Technologies Used

| Component           | Technology         |
|---------------------|--------------------|
| Model Training      | Jupyter Notebook (Python, scikit-learn) |
| Backend API         | FastAPI            |
| Frontend            | Streamlit          |
| Experiment Tracking | MLflow             |
| Deployment          | Render (backend), Streamlit Cloud (frontend) |
| Optional Container  | Docker             |

---

## Step-by-Step Guide

### 1. Model Training

- Used the **Iris dataset** (4 features, 3 classes).
- Checked for missing values (none in Iris dataset).
- Preprocessed data (scaling not needed for tree-based model).
- Trained a **Random Forest Classifier**.
- Logged model parameters, metrics (accuracy, precision, recall), and training time to **MLflow**.
- Saved the trained model as `model.pkl` using `joblib`.

### 2. Backend API (FastAPI)

- Created FastAPI app (`backend/main.py`).
- Loaded the saved `model.pkl` at startup.
- Created `/predict` POST endpoint that accepts JSON input with flower features.
- Endpoint returns predicted Iris class.
- API documentation automatically available at `/docs`.

### 3. Frontend (Streamlit)

- Built interactive Streamlit app (`frontend/streamlit_app.py`).
- User inputs sepal length, sepal width, petal length, and petal width.
- On submission, app sends POST request to FastAPI `/predict` endpoint.
- Displays prediction result on the UI.

### 4. Experiment Tracking (MLflow)

- Used MLflow to track:
  - Model parameters (number of trees, etc.)
  - Accuracy, precision, recall
  - Training duration


### 5. Deployment

- **Backend:** Deployed FastAPI app on [Render](https://render.com).
  - Backend URL: `https://iris-prediction-2.onrender.com`
- **Frontend:** Deployed Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud).
- Both services run in containerized environments managed by the platform.
- (Optional) Dockerfile added for manual containerization (if applicable).

---

## How to Run Locally

1. Clone the repository:
    
    git clone https://github.com/1323saman/iris-prediction.git
  
    

2. Create and activate virtual environment:
   
    py -m venv ML
   
    .\ML\Scripts\activate   
  

3. Install dependencies:
    
    py -m pip install -r requirements.txt
  

4. Run FastAPI backend:
   
    uvicorn Backend.main:app --reload
  

5. Run Streamlit frontend:
    
    streamlit run Frontend/streamlit_app.py
    

6. Open browser:
    - Backend Swagger UI: `http://127.0.0.1:8000/docs`
    - Streamlit app: `http://localhost:8501`

---

Notes on Dockerization
This project is deployed on Render and Streamlit Cloud, which manage Docker containers automatically.

No manual Dockerfile is required but can be added for custom container builds.

References
- FastAPI Documentation
- Streamlit Documentation
- MLflow Documentation
- Render Deployment Guide

Contact
For any questions, please contact:
Saman Sajid
Email: samansajid0158@gmail.com


