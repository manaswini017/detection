# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model & accuracy
model = joblib.load("fake_account_model.pkl")
with open("model_accuracy.txt", "r") as f:
    model_accuracy = float(f.read())

st.title("📷 Instagram Fake Account Detection")
st.write(f"**Model Accuracy:** {model_accuracy*100:.2f}%")

# Input form
followers = st.number_input("Number of Followers", min_value=0, step=1)
following = st.number_input("Number of Following", min_value=0, step=1)
posts = st.number_input("Number of Posts", min_value=0, step=1)
bio_length = st.number_input("Bio Length (characters)", min_value=0, step=1)
has_profile_pic = st.selectbox("Has Profile Picture?", ["Yes", "No"])
engagement_rate = st.number_input("Engagement Rate (0.0 - 1.0)", min_value=0.0, max_value=1.0, step=0.01)

# Convert Yes/No to 1/0
has_profile_pic_val = 1 if has_profile_pic == "Yes" else 0

if st.button("Predict"):
    input_df = pd.DataFrame({
        "followers": [followers],
        "following": [following],
        "posts": [posts],
        "bio_length": [bio_length],
        "has_profile_pic": [has_profile_pic_val],
        "engagement_rate": [engagement_rate]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][prediction] * 100

    if prediction == 1:
        st.error(f"🚨 This account is likely FAKE ({probability:.2f}% confidence)")
    else:
        st.success(f"✅ This account is likely GENUINE ({probability:.2f}% confidence)")
