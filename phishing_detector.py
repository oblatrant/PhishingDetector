# phishing_detector.py

"""
PhishDetect: A simple Machine Learning Phishing Email Detector
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Make sure you put your dataset CSV in the 'dataset' folder
dataset_path = "dataset/phishing_emails.csv"
print("Loading dataset...")
try:
    data = pd.read_csv(dataset_path)
except FileNotFoundError:
    print(f"Dataset not found at {dataset_path}. Please place your CSV file there.")
    exit()

# Quick look at the data
print("Dataset loaded. First 5 rows:")
print(data.head())


email_texts = data["text_combined"]  # your email text column
labels = data["label"]               # 0=Legit, 1=Phishing

# Convert text to numerical
vectorizer = TfidfVectorizer(stop_words="english")
email_features = vectorizer.fit_transform(email_texts)


X_train, X_test, y_train, y_test = train_test_split(
    email_features, labels, test_size=0.2, random_state=42
)


# Train the Machine Learning model
model = MultinomialNB()
model.fit(X_train, y_train)
print("\nModel trained successfully!")

# Evaluate model accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy*100:.2f}%")


SUSPICIOUS_KEYWORDS = [
    "urgent", "verify", "account", "password", "login",
    "click", "security alert", "confirm", "suspend"
]


def check_email(email_text):
    """
    Takes an email as input and predicts if it's phishing or legitimate.
    Uses both ML model and keyword check for overall consensus.
    """
    # ML prediction
    email_vector = vectorizer.transform([email_text])
    ml_prediction = model.predict(email_vector)[0]  # 0 or 1

    # Rule-based keyword check
    keyword_score = sum(
        1 for word in SUSPICIOUS_KEYWORDS if word.lower() in email_text.lower()
    )

    # Overall consensus: phishing if either ML predicts phishing or keywords are found
    if ml_prediction == 1 or keyword_score > 0:
        return "Phishing Email"
    else:
        return "Legitimate Email"


print("\n--- Test Your Own Email ---")
print("Paste your email below. When done, type 'END' on a new line and press Enter.\n")

while True:
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":  # end of email
            break
        lines.append(line)
    
    email_text = "\n".join(lines).strip()
    
    if not email_text:
        print("No email entered. Try again or type 'exit' to quit.")
        continue
    if email_text.lower() == "exit":
        break
    
    result = check_email(email_text)
    print(f"\nOverall Verdict: {result}\n")
