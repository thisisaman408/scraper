# MyScraper

MyScraper is a web scraping Python library that uses Large Language Models (LLMs) and direct graph logic to create powerful scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.).

Just say which information you want to extract and the library will do it for you!

## Quick Install

```bash
pip install my_scraper

# IMPORTANT (for fetching websites content)
playwright install
```

## Usage

```python
from my_scraper.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage.",
    source="https://example.com/",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

## License

MIT License
