# Emotion-Recognizing-AI-Chatbot

Welcome to the **Emotion-Recognizing AI Chatbot**! This project aims to create an intelligent chatbot that can recognize the emotions of text inputs, enabling more empathetic and context-aware responses.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)

## Introduction
The Emotion-Recognizing AI Chatbot is designed to detect emotions in user messages and respond appropriately, improving user experience in areas like mental health support, customer service, or simply as an emotional companion. By using natural language processing (NLP) and machine learning, the chatbot can classify the emotions behind messages as happiness, sadness, anger, and more.

## Features
- Emotion detection for text inputs.
- Customizable responses based on detected emotions.
- Interactive chat interface built using Streamlit.
- Pre-trained machine learning model for emotion classification.

## Installation
To get started, you need to clone this repository and set up the environment:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/PavanKrishna19/Emotion-Recognizing-AI-Chatbot.git
   cd Emotion-Recognizing-AI-Chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Train the Model** (Optional): If you'd like to train the model with a new dataset, use:
   ```sh
   python main.py
   ```

2. **Run the Chatbot Interface**:
   Use Streamlit to start the chatbot interface:
   ```sh
   streamlit run streamlit_app/streamlit_ui.py
   ```

3. **Interacting with the Chatbot**:
   Open the provided local URL in your browser and start chatting! The chatbot will recognize your emotions and respond accordingly.

## Technologies Used
- **Python**: Main programming language.
- **Pandas & NumPy**: Data preprocessing.
- **Scikit-Learn**: Machine learning model training.
- **NLTK**: Natural language processing.
- **Streamlit**: Web interface for the chatbot.

## Dataset
The chatbot is trained on an emotion dataset containing labeled text samples. The dataset used includes various emotions such as happiness, sadness, anger, and fear. You can replace the dataset with your own to retrain the model.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

1. **Fork the Repository**.
2. **Create a Branch** (`git checkout -b feature-branch`).
3. **Commit Your Changes** (`git commit -m 'Add new feature'`).
4. **Push to Your Branch** (`git push origin feature-branch`).
5. **Open a Pull Request**.

## Troubleshooting
If you encounter issues while running the project, here are some common solutions:

- **Module Not Found**: Ensure you have activated the virtual environment and installed all dependencies using `pip install -r requirements.txt`.
- **Port Already in Use**: If Streamlit shows an error that the port is already in use, try specifying a different port:
  ```sh
  streamlit run streamlit_app/streamlit_ui.py --server.port 8502
  ```
- **Model File Not Found**: Make sure you have the `model.pkl` and `vectorizer.pkl` files in the correct directory (`models/`). If not, you may need to retrain the model using `python main.py`.

## Future Improvements
Here are some potential areas for future development:

- **Multilingual Emotion Detection**: Extend the model to support multiple languages, enabling broader user interaction.
- **Voice Input**: Add support for voice input and emotion recognition through audio analysis.
- **Enhanced Emotion Categories**: Expand the range of detectable emotions for more nuanced interactions.
- **Improved Interface**: Enhance the Streamlit interface for a better user experience, including richer visual feedback and more user-friendly controls.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

