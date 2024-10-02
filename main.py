import streamlit as st
from crew import crew


st.title("Personalized AI Education Agents")


topic = st.text_input("Topic")
time = st.text_input("Time")
current_level = st.selectbox("Current Level", ["beginner", "intermediate", "advanced"], index=1)
others = st.text_area("Other things you would like us to know")


if st.button("Submit"):
    crew.kickoff(inputs={'topic': topic, 'time': time, 'current_level': current_level, 'others': others})
    with open('result.md', 'r') as f:
        result = f.read()
    st.write(result)
