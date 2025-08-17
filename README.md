# Fake Account Detection on Social Media Platforms

## Overview
## Project Description

This project implements a machine learning-based system to detect fake accounts on social media platforms like Instagram. The goal is to identify suspicious or fraudulent account
using account-related features such as number of followers, following, posts, bio length, engagement rate, and profile picture availability.
The system provides predictions with confidence scores to classify accounts as either Genuine or Fake, thereby improving online trust and security.


---

## Features
- Preprocessing of dataset containing account statistics
- Feature extraction (followers, following, posts, bio length, engagement rate, profile picture)
- Machine learning model training using algorithms like Random Forest, Logistic Regression, and Decision Tree
- Prediction of whether an account is fake or genuine
- Streamlit-based web interface for easy interaction
- Confidence percentage displayed for predictions


---

## Technologies Used
- Python
- pandas, scikit-learn, numpy, matplotlib, seaborn
- Streamlit (for web interface)
- Dataset: Custom dataset of Instagram account features (CSV format)


---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # For Windows
source venv/bin/activate # For Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage
Run the App
```bash
streamlit run app.py
```


## Steps
- Upload dataset (CSV file with account details) or enter details manually
- The trained model will predict whether the account is Fake or Genuine
- Confidence score will be displayed

---

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- scikit-learn for ML algorithms
- Streamlit for building web app
- pandas & numpy for data handling
- matplotlib & seaborn for visualization
---
## Future Work
- Expand dataset with real-world social media account data.
- Integrate deep learning models for improved accuracy.
- Connect with social media APIs for real-time detection.
- Deploy on cloud platforms for wider accessibility.
- --
