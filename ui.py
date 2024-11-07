import streamlit as st
import requests

st.title("Cryptocurrency Query App")
session_id = st.text_input("Session ID")
query = st.text_area("Your query")
source_language = st.selectbox("Select Source Language", ["English", "Tamil", "Hindi", "Spanish", "French", "German", "Italian", "Chinese", "Japanese", "Arabic", "Russian"])

if st.button("Submit"):
    response = requests.post("http://0.0.0.0:8001/query", json={"session_id": session_id, "query": query, "source_language": source_language})
    if response.status_code == 200:
        st.write(response.json()["response"])
    else:
        st.write("Error:", response.json()["detail"])
