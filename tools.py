from crewai_tools import SerperDevTool, YoutubeVideoSearchTool
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
search_tool = SerperDevTool()
yt_tool= YoutubeVideoSearchTool()