Iris Flower Prediction App
This project is a simple machine learning application that predicts the species of an Iris flower based on its features (sepal length, sepal width, petal length, petal width).

Project Structure
Backend: FastAPI API that serves the prediction model.

Frontend: Streamlit app that takes user input and shows prediction results.

Machine Learning: Uses a pre-trained model and scaler saved as pickle files.

How to Run
Run the backend API:


uvicorn ml.main:app --reload
Run the frontend app:

streamlit run Frontend/app.py
Open the Streamlit app in your browser and enter Iris flower features to get a prediction.

API Endpoint
POST /predict: Accepts JSON input with Iris flower features and returns the predicted species.

Deployment
This project can be deployed on cloud platforms such as Azure App Service or AWS EC2. Optionally, Docker can be used for containerization.

Tools & Technologies
Python, FastAPI

Streamlit

Scikit-learn (for ML model)

Uvicorn (for running FastAPI)

Requests (for API calls)

Make sure the backend is running before starting the frontend.

Update the API URL in the frontend code if deploying on a remote server.
