import streamlit as st
from crew import crew

# Title of the app
st.title("Personalized AI Education Agents")

# Input fields
topic = st.text_input("Topic")
time = st.text_input("Time")
current_level = st.selectbox("Current Level", ["beginner", "intermediate", "advanced"], index=1)
others = st.text_area("Others")

# Submit button
if st.button("Submit"):
    # Display the input values
    # st.write("## Input Summary")
    # st.write(f"**Topic:** {topic}")
    # st.write(f"**Time:** {time}")
    # st.write(f"**Current Level:** {current_level}")
    # st.write(f"**Others:** {others}")
    crew.kickoff(inputs={'topic': topic, 'time': time, 'current_level': current_level, 'others': others})
    with open('result.md', 'r') as f:
        result = f.read()
    st.write(result)
