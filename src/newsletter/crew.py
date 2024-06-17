from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from newsletter.tools.custom_tool import SearchAndContent, FindSimilar, GetContents
# from langchain_anthropic import ChatAnthropic
# Uncomment the following line to use an example of a custom tool
# from newsletter.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class NewsletterCrew:
    """Newsletter crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def llm(self):
        llm = ChatAnthropic(model_name="claude-3-sonnet-20240229", max_tokens=4096)
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SearchAndContent(), FindSimilar(), GetContents()],
            verbose=True,

        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            tools=[SearchAndContent(), FindSimilar(), GetContents()],
            verbose=True,
        )

    @agent
    def designer(self) -> Agent:
        return Agent(
            config=self.agents_config["designer"],
            tools=[SearchAndContent(), FindSimilar(), GetContents()],
            verbose=True,
            allow_delegation=False,  # This agent can't delegate,
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    @task
    def edit_task(self) -> Task:
        return Task(
            config=self.tasks_config["edit_task"],
            agent=self.editor(),
        )

    @task
    def newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config["newsletter_task"],
            agent=self.designer(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Newsletter crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
