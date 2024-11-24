from app.model import load_model

class EmotionChatbot:
    def __init__(self):
        self.vectorizer, self.model = load_model()

    def predict_emotion(self, text):
        """Predict the emotion of a given text."""
        text_vec = self.vectorizer.transform([text])
        prediction = self.model.predict(text_vec)
        return prediction[0]