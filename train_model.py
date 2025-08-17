# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("dataset/instagram_fake_accounts.csv")

# Features & Target
X = data.drop("is_fake", axis=1)
y = data["is_fake"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save model & accuracy
joblib.dump(model, "fake_account_model.pkl")
with open("model_accuracy.txt", "w") as f:
    f.write(str(accuracy))
