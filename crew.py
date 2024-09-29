from crewai import Crew,Process
from agents import researcher,writer
from tasks import research_task,write_task


crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  
)


# result=crew.kickoff(inputs={'topic':'ai agents', 'time': '3hrs', 'current_level': 'intermediate', 'others': 'i have previous experience with openai api'})
# print(result)