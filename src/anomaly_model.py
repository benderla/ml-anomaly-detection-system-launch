from sklearn.ensemble import IsolationForest
import pandas as pd

def train_model(data):

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(data)

    return model