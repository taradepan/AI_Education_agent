from crewai import Task
from tools import search_tool, yt_tool
from agents import researcher, writer

tool=[search_tool, yt_tool]

research_task = Task(
    description=(
        "Conduct thorough research on avaliable courses or tutorials using internet resources based on provided info: '{topic}' . "
        "Focus on gathering best courses. if the user ask for blog articles or reading material only then no need to search on youtube. also check for reviews for the course material if possible."
    ),
    expected_output=(
        "some of the best courses or tutorials (with Links) based on the provided info from the user :'{topic}'."
    ),
    tools=tool,
    agent=researcher,
)


write_task = Task(
    description=(
        "Using the research details, write an currated list for the user based on the provided requirements: '{topic}'. "
        "Ensure the content is valid and provide the links to access them."
    ),
    expected_output='A completely curriated list of courses and tutorials suitable for {topic}, formatted in markdown.',
    tools=tool,
    agent=writer,
    async_execution=False,
    output_file='blog-post.md'  
)