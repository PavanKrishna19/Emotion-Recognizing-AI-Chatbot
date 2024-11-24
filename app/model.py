import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle
from app.preprocess import clean_text

def train_model():
    """Train and save the emotion recognition model."""
    # Load dataset
    data = pd.read_csv('data/emotions_dataset.csv')
    data = data.dropna(subset=['Text', 'Emotion'])  # Drop rows with missing values in key columns
    data['Text'] = data['Text'].apply(clean_text)

    # Features and Labels
    X = data['Text']
    y = data['Emotion']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train Logistic Regression
    model = LogisticRegression()
    model.fit(X_train_vec, y_train)

    # Evaluate model
    y_pred = model.predict(X_test_vec)
    print(classification_report(y_test, y_pred))

    # Save vectorizer and model
    os.makedirs('models', exist_ok=True)
    with open('models/vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
    with open('models/model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

def load_model():
    """Load the emotion recognition model and vectorizer."""
    with open('models/vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    with open('models/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return vectorizer, model