import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import joblib

# Load the classifier model
pipe = joblib.load(open('./models/emotion_classifier.pkl','rb'))

def predict_emotions(classifier, docx):
    results = pipe.predict([docx])
    return results[0]

def get_prediction_proba(classifier, docx):
    results = pipe.predict_proba([docx])
    return results[0]

emotions_emoji_dict = {'anxiety': '😰','depression': '😞','happy': '😊',
                       'stress': '😓'}

# Main Application
def main():
    st.title("Emotion Classifier App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home-Emotion In Text")

        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label='Submit')

        if submit_text:
            col1, col2 = st.columns(2)

            # Apply Fxn Here
            prediction = predict_emotions(pipe, raw_text)
            probability = get_prediction_proba(pipe, raw_text)
            
            with col1:
                st.success("Original Text")
                st.write(raw_text)

                st.success("Prediction")
                emoji_icon = emotions_emoji_dict[prediction]
                st.write("{} : {}".format(prediction, emoji_icon))
                st.write("Confidence : {}".format(round(np.max(probability),2)))

            with col2:
                st.success("Prediction Probability")
                proba_df = pd.DataFrame({'emotions': pipe.classes_, 'probability': probability})
                fig = alt.Chart(proba_df).mark_bar().encode(x='emotions', y='probability', color='emotions')
                st.altair_chart(fig, use_container_width=True)

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
