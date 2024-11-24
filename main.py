import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Load dataset
def load_dataset(filepath):
    data = pd.read_csv(filepath)
    return data

# Train model
def train_model(data):
    # Text and labels
    data = data.dropna(subset=['Text', 'Emotion'])  # Drop rows with missing values in key columns
    X = data['Text']  # Update to match the actual text column name
    y = data['Emotion']  # Update to match the actual emotion label column name

    # Vectorize text
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

    # Train model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Evaluate
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    return vectorizer, model

# Save model and vectorizer
def save_model(vectorizer, model, save_dir='models'):
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, 'vectorizer.pkl'), 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
    with open(os.path.join(save_dir, 'model.pkl'), 'wb') as model_file:
        pickle.dump(model, model_file)
    print(f"Model and vectorizer saved in '{save_dir}'.")

# Main function
if __name__ == "__main__":
    dataset_path = 'data/emotions_dataset.csv'  # Update with your actual dataset path
    data = load_dataset(dataset_path)

    vectorizer, model = train_model(data)
    save_model(vectorizer, model)
