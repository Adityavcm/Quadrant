import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("../data/exoplanet.csv")

features = df[
    [
        "Orbital period",
        "transit duration",
        "radii(planet)",
    ]
]
target = df["Exo status"]

X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)


def predict_exoplanet_status(X_test):
    y_pred = model.predict(X_test)

    return y_pred


accuracy = accuracy_score(y_test, predict_exoplanet_status(X_test))
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predict_exoplanet_status(X_test)))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predict_exoplanet_status(X_test)))
