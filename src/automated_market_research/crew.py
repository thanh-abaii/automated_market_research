import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool  #, DataAnalysisTool, TextGenerationTool
import os
from pathlib import Path

# Base directory where this script is located
BASE_DIR = Path(__file__).resolve().parent

@CrewBase
class AutomatedMarketResearch:
    """AutomatedMarketResearch crew"""

    # Use absolute paths for configuration files
    agents_config_path = BASE_DIR / 'config' / 'agents.yaml'
    tasks_config_path = BASE_DIR / 'config' / 'tasks.yaml'

    def __init__(self):
        # Debug YAML parsing
        try:
            with open(self.agents_config_path, 'r') as f:
                self.agents_config = yaml.safe_load(f)
                print("Agents Config Loaded:", self.agents_config)

            with open(self.tasks_config_path, 'r') as f:
                self.tasks_config = yaml.safe_load(f)
                print("Tasks Config Loaded:", self.tasks_config)

        except Exception as e:
            print(f"Error loading configuration files: {e}")
            raise

    @agent
    def data_gatherer(self) -> Agent:
        """Defines the Data Gatherer Agent"""
        return Agent(
            config=self.agents_config['data_gatherer'],
            tools=[ScrapeWebsiteTool()],  # Add web scraping capabilities
            verbose=True
        )

    @agent
    def analysis_agent(self) -> Agent:
        """Defines the Analysis Agent"""
        return Agent(
            config=self.agents_config['analysis_agent'],
            # tools=[DataAnalysisTool()],  # Add data analysis capabilities
            verbose=True
        )

    @agent
    def report_generator(self) -> Agent:
        """Defines the Report Generator Agent"""
        return Agent(
            config=self.agents_config['report_generator'],
            # tools=[TextGenerationTool()],  # Add text generation capabilities
            verbose=True
        )

    @task
    def data_gathering_task(self) -> Task:
        """Task for data gathering"""
        print("Config for data_gathering_task:", self.tasks_config['data_gathering_task'])  # Debugging
        return Task(
            config=self.tasks_config['data_gathering_task'],  # Ensure this resolves to a valid dictionary
            agent=self.data_gatherer(),  # Call the method to get the Agent object
            verbose=True
    )

    @task
    def data_analysis_task(self) -> Task:
        """Task for data analysis"""
        return Task(
            config=self.tasks_config['data_analysis_task'],
            agent=self.analysis_agent(),  # Call the method to get the Agent object
            verbose=True
        )

    @task
    def report_generation_task(self) -> Task:
        """Task for report generation"""
        return Task(
            config=self.tasks_config['report_generation_task'],
            agent=self.report_generator(),  # Call the method to get the Agent object
            output_file='output/market_research_report.md',
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
