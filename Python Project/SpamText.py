"""
Spam/Ham Text Classifier
-------------------------
A simple, explainable ML pipeline: TF-IDF vectorization + Logistic Regression.
Built as a portfolio project to demonstrate the full ML workflow:
data -> preprocessing -> train/test split -> model training -> evaluation.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# 1. Load data
df = pd.read_csv("messages.csv")
print(f"Loaded {len(df)} messages ({df['label'].value_counts().to_dict()})")

X = df["text"]
y = df["label"]

# 2. Train/test split (80/20, stratified so both classes are balanced in each split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")

# 3. Feature extraction: TF-IDF turns text into weighted word-frequency vectors
vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 4. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 5. Evaluate
y_pred = model.predict(X_test_vec)

print("\n--- Evaluation on held-out test set ---")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='spam'):.2f}")
print(f"Recall:    {recall_score(y_test, y_pred, pos_label='spam'):.2f}")
print(f"F1 Score:  {f1_score(y_test, y_pred, pos_label='spam'):.2f}")

print("\nConfusion Matrix (rows=actual, cols=predicted):")
labels = ["ham", "spam"]
cm = confusion_matrix(y_test, y_pred, labels=labels)
print(f"pred_ham  pred_spam")
for i, row_label in enumerate(labels):
    print(f"actual_{row_label:<5} {cm[i][0]:^9} {cm[i][1]:^9}")

print("\nFull classification report:")
print(classification_report(y_test, y_pred))

# 6. Try it on new, unseen messages
print("\n--- Testing on brand-new messages ---")
new_messages = [
    "Congratulations! Click here to claim your free prize now",
    "Hey, are you coming to the study group tonight?",
    "URGENT: verify your bank account immediately or it will be locked",
    "Can you send me the meeting notes from today?",
]
new_vec = vectorizer.transform(new_messages)
predictions = model.predict(new_vec)
probabilities = model.predict_proba(new_vec)

for msg, pred, prob in zip(new_messages, predictions, probabilities):
    confidence = max(prob) * 100
    print(f"[{pred.upper():5}] ({confidence:.1f}% confident) -> {msg}")
