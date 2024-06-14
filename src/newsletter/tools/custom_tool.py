import os
from crewai_tools import BaseTool
from exa_py import Exa


class SearchAndContent(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. Results are only from the last week. Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        return "this is an example of a tool output, ignore it and move along."
