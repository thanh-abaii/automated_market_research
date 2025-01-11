from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebScraperTool, DataAnalysisTool, TextGenerationTool

@CrewBase
class AutomatedMarketResearch:
    """AutomatedMarketResearch crew"""

    # Load configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_gatherer(self) -> Agent:
        """Defines the Data Gatherer Agent"""
        return Agent(
            config=self.agents_config['data_gatherer'],
            tools=[WebScraperTool()],  # Add web scraping capabilities
            verbose=True
        )

    @agent
    def analysis_agent(self) -> Agent:
        """Defines the Analysis Agent"""
        return Agent(
            config=self.agents_config['analysis_agent'],
            tools=[DataAnalysisTool()],  # Add data analysis capabilities
            verbose=True
        )

    @agent
    def report_generator(self) -> Agent:
        """Defines the Report Generator Agent"""
        return Agent(
            config=self.agents_config['report_generator'],
            tools=[TextGenerationTool()],  # Add text generation capabilities
            verbose=True
        )

    @task
    def data_gathering_task(self) -> Task:
        """Task for data gathering"""
        return Task(
            config=self.tasks_config['data_gathering_task'],
            agent=self.data_gatherer,  # Assign task to Data Gatherer Agent
            verbose=True
        )

    @task
    def data_analysis_task(self) -> Task:
        """Task for data analysis"""
        return Task(
            config=self.tasks_config['data_analysis_task'],
            agent=self.analysis_agent,  # Assign task to Analysis Agent
            verbose=True
        )

    @task
    def report_generation_task(self) -> Task:
        """Task for report generation"""
        return Task(
            config=self.tasks_config['report_generation_task'],
            agent=self.report_generator,  # Assign task to Report Generator Agent
            output_file='output/market_research_report.md',  # Save output to a markdown file
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Automated Market Research Crew"""
        return Crew(
            agents=self.agents,  # Agents are automatically created by @agent decorators
            tasks=self.tasks,    # Tasks are automatically created by @task decorators
            process=Process.sequential,  # Execute tasks in sequence
            verbose=True,
        )
