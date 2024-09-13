from crewai import Agent
from tools import search_tool, yt_tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model_name="llama-3.1-70b-versatile", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"),)

tool=[search_tool, yt_tool]

researcher=Agent(
    role='Researcher',
    goal='Collect detailed information based on the given topic from the internet.',
    verbose=True,
    memory=True,
    backstory=(
       "You are a diligent researcher adept at gathering information from various online sources like online search and youtube." 
    ),
    tools=tool,
    llm=llm,
    allow_delegation=True,
)


writer=Agent(
    role='Blog Writer',
    goal='Write a list of suitable courses based on the users input, refer the collected data from the internt. provide the linkes to those resourses.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in suggesting courses and tutorials for people at different levels based on their requirements."
    ),
    tools=tool,
    llm=llm,
    allow_delegation=False,
)