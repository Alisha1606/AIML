#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Define pairs of patterns and responses for the chatbot
pairs = [
    ["hi|hello|hey", ["Hello! I'm your medical chatbot. How can I assist you today?", "Hey there! I'm here to provide medical information. What do you need help with?"]],
    ["how are you?", ["I'm just a chatbot, so I don't have feelings, but I'm ready to assist you with any medical queries.", "I'm functioning well and ready to help you. What can I do for you?"]],
    ["what is your name?", ["You can call me MediBot. I'm designed to answer medical-related questions.", "I'm MediBot, your medical assistant."]],
    ["what can you do?", ["I can provide information about symptoms, treatments, diagnoses, and more related to medical conditions.", "I'm here to answer your medical questions and provide accurate information."]],
    ["how to use this chatbot?", ["You can start by typing a medical-related question or topic you want to know more about. For example, you can ask about symptoms, treatments, or general medical advice.", "Simply type your medical query, and I'll do my best to provide you with relevant information."]],
    ["advanced question", ["I'm ready to answer more complex medical questions. Please go ahead and ask.", "Feel free to ask any advanced medical questions you have. I'll do my best to provide detailed information."]],
    ["general health tips", ["Maintaining a balanced diet and regular exercise are important for overall health.", "Getting enough sleep and managing stress are key components of good health."]],
    ["emergency response", ["In case of emergency, dial emergency services immediately.", "For medical emergencies, seek immediate medical attention."]],
    ["what is your name?", ["You can call me ChatBot.", "My name is ChatBot."]],
    ["tell me about the medical chatbot", ["The medical chatbot is designed to provide accurate medical information through natural language interaction."]],
    ["how can I use the medical chatbot?", ["You can start by asking general medical questions or specific queries about symptoms, diseases, or treatments."]],
    ["what kind of information can the chatbot provide?", ["The chatbot can provide information on various medical conditions, treatment options, preventive measures, and general health advice."]],
    ["can the chatbot diagnose illnesses?", ["No, the chatbot cannot diagnose illnesses. It provides information and guidance based on the input provided."]],
    ["what technologies are used in the chatbot?", ["The chatbot uses natural language processing (NLP) techniques and a knowledge base of medical information to generate responses."]],
    ["how accurate is the information provided by the chatbot?", ["The information provided by the chatbot is based on reputable medical sources, but users should always consult healthcare professionals for accurate diagnosis and treatment."]],
    ["flu", ["Common symptoms of flu include fever, cough, and body aches.", "Flu can be treated with rest, fluids, and sometimes antiviral medications."]],
    ["diabetes", ["Diabetes is a condition where blood sugar levels are too high.", "Treatment for diabetes includes medication, diet, and exercise."]],
    ["asthma", ["Asthma is a chronic respiratory condition that can cause wheezing and shortness of breath.", "Asthma is managed with inhalers and avoiding triggers."]],
    ["hypertension", ["Hypertension, or high blood pressure, increases the risk of heart disease and stroke.", "Managing hypertension involves medication and lifestyle changes."]],
    ["depression", ["Depression is a mental health disorder characterized by persistent sadness and loss of interest.", "Treatment for depression may include therapy and medication."]],
    ["cancer", ["Cancer is a disease where abnormal cells divide uncontrollably and invade tissues.", "Cancer treatment varies depending on the type and stage, including surgery, chemotherapy, and radiation therapy."]],
    ["heart attack", ["A heart attack occurs when blood flow to the heart is blocked, leading to damage.", "Immediate medical attention is crucial for a heart attack, including aspirin and emergency procedures."]],
    ["stroke", ["A stroke is a medical emergency where blood flow to the brain is disrupted, leading to brain damage.", "Recognizing symptoms like facial drooping and speech difficulties is important for stroke care."]],
    ["sepsis", ["Sepsis is a severe infection that can lead to organ failure and death if not treated promptly.", "Early recognition and antibiotic treatment are critical for sepsis."]],
    ["trauma", ["Trauma refers to physical injuries caused by accidents or violence.", "Managing trauma involves first aid, medical evaluation, and appropriate treatment."]],
    ["quit", ["Goodbye!", "Take care!"]]
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(pairs, reflections)

# Main function to run the chatbot within Streamlit
def main():
    st.title("MEDICAL CHATBOT")
    st.write("Welcome to the ChatBot!")
    st.write("Type your messages below.")

    # Counter for generating unique keys
    counter = 0

    while True:
        counter += 1  # Increment counter for each iteration
        user_input = st.text_input(f"You {counter}:")

        # Display "Ready" button after user input
        ready_button_key = f"ready_button_{counter}"  # Unique key for "Ready" button
        if st.button("Send", key=ready_button_key) and user_input:
            response = chatbot.respond(user_input)

            # Display chatbot response
            st.write("ChatBot:", response)

if __name__ == "__main__":
    main()

