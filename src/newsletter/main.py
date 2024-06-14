#!/usr/bin/env python
from newsletter.crew import NewsletterCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    NewsletterCrew().crew().kickoff(inputs=inputs)