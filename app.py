import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

st.title('Movie Review Sentiment Analysis')
review = st.text_area('Enter a movie review:')

def main():
        if review.strip():
            transformed_review = vectorizer.transform([review])
            prediction = model.predict(transformed_review)[0]
            sentiment = 'Positive' if prediction == 'positive' else 'Negative'
            st.write(f'The sentiment is: **{sentiment}**')
        else:
            st.write('Please enter a valid review.')

if __name__ == "__main__":
    if st.button('Predict'):
        main()

# myenv\Scripts\activate
# streamlit run app.py        
