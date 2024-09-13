from crewai import Crew,Process
from agents import researcher,writer
from tasks import research_task,write_task


crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  
)


result=crew.kickoff(inputs={'topic':'I want to learn about AI Agents. I know how to use openai api.'})
print(result)