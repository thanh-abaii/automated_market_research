#!/usr/bin/env python
import sys
import warnings
import asyncio
import platform

from automated_market_research.crew import AutomatedMarketResearch

# Compatibility fix for Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally. Replace the inputs below with relevant values
# for your automated market research project.

def run():
    """
    Run the crew for automated market research.
    """
    inputs = {
        'product_category': 'AI-driven tools'  # Replace with desired product category
    }
    try:
        AutomatedMarketResearch().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations (optional).
    """
    inputs = {
        "product_category": "AI-driven tools"  # Replace with desired product category
    }
    try:
        AutomatedMarketResearch().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AutomatedMarketResearch().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results (optional).
    """
    inputs = {
        "product_category": "AI-driven tools"  # Replace with desired product category
    }
    try:
        AutomatedMarketResearch().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
