import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from taxifare.ml_logic.preprocessor import preprocess_features
from taxifare.ml_logic import model
from taxifare.interface.main import pred
app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2014-07-06+19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2
@app.get("/predict")
def predict(
        pickup_datetime: str,  # 2014-07-06 19:18:00
        pickup_longitude: float,    # -73.950655
        pickup_latitude: float,     # 40.783282
        dropoff_longitude: float,   # -73.984365
        dropoff_latitude: float,    # 40.769802
        passenger_count: int
    ):      # 1
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """
    X = pd.DataFrame({'pickup_datetime': [pickup_datetime],
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "passenger_count": [passenger_count]})
    X['pickup_datetime'] = pd.Timestamp(pickup_datetime,tz="US/Eastern")
    y_pred=pred(X)
    return {'fare': float(y_pred)}

@app.get("/")
def root():
    print('hello')
    return{'greeting': 'Hello'}
