import json
import os
from my_scraper.graphs import SmartScraperGraph

from pydantic import BaseModel, Field
from typing import List

# 1. Define the exact structure we want the AI to output
class Article(BaseModel):
    title: str = Field(description="The headline of the article")
    url: str = Field(description="The link to the article")
    points: int = Field(description="The number of upvotes or points")
    author: str = Field(description="The username of the person who posted it")

class HackerNewsData(BaseModel):
    articles: List[Article] = Field(description="The top 5 articles on the page")

# 2. Configuration setup
graph_config = {
    "llm": {
        "api_key": os.getenv("GROQ_API_KEY", "YOUR_API_KEY_HERE"),
        "model": "groq/llama-3.3-70b-versatile", 
    },
    "verbose": True,
    "headless": True,
}

# 3. Define the scraping task with the schema
smart_scraper = SmartScraperGraph(
    prompt="Extract the top 5 articles from the page with their details.",
    source="https://news.ycombinator.com/",
    config=graph_config,
    schema=HackerNewsData
)

# 4. Run the AI scraper
print("Starting the AI scraper... Please wait.")
result = smart_scraper.run()

# 4. Print out the structured data!
print("\n--- RESULTS ---")
print(json.dumps(result, indent=4))
