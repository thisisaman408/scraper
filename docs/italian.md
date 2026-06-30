## 🚀 **Cerchi un modo ancora più veloce e semplice per fare scraping su larga scala (con sole 5 righe di codice)?** Scopri la nostra versione potenziata su [**MyScraper.com**](https://my_scraper.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&utm_content=top_banner)! 🚀

---

# 🕷️ MyScraper: You Only Scrape Once

<p align="center">
  <a href="https://my_scraper.com">
    <img src="https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/media/banner.png" alt="MyScraper" style="width: 100%;">
  </a>
</p>

[English](../README.md) | [中文](chinese.md) | [日本語](japanese.md)
| [한국어](korean.md)
| [Русский](russian.md) | [Türkçe](turkish.md)
| [Deutsch](german.md)
| [Español](spanish.md)
| [français](french.md)
| [Português](portuguese.md)
| [Italiano](italian.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/my_scraper?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/my_scraper)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://dcbadge.vercel.app/api/server/gkxQDAjfeX)](https://discord.gg/gkxQDAjfeX)
<p align="center">
<a href="https://trendshift.io/repositories/15078" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15078" alt="MyScraper%2FScrapegraph-ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<p align="center">

[MyScraper](https://my_scraper.com) è una libreria Python per il *web scraping* che utilizza LLM e logica basata sui grafi per creare pipeline di scraping per siti web e documenti locali (XML, HTML, JSON, Markdown, ecc.).

Indica semplicemente quali informazioni vuoi estrarre e la libreria lo farà per te!
<p align="center">
  <img src="https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="MyScraper Hero" style="width: 100%;">
</p>


## 🚀 Integrazioni

MyScraper offre integrazioni con i framework e gli strumenti più diffusi per potenziare le tue capacità di scraping. Che tu stia sviluppando in Python o Node.js, usando framework LLM o piattaforme no-code, offriamo un'ampia gamma di opzioni di integrazione.

Puoi trovare ulteriori informazioni al seguente [link](https://my_scraper.com)

**Integrazioni**:
- **API**: [Documentazione](https://docs.my_scraper.com/introduction)
- **SDK**: [Python](https://docs.my_scraper.com/sdks/python), [Node](https://docs.my_scraper.com/sdks/javascript)
- **Framework LLM**: [Langchain](https://docs.my_scraper.com/integrations/langchain), [Llama Index](https://docs.my_scraper.com/integrations/llamaindex), [Crew.ai](https://docs.my_scraper.com/integrations/crewai), [Agno](https://docs.my_scraper.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **Framework Low-code**: [Pipedream](https://pipedream.com/apps/my_scraper), [Bubble](https://bubble.io/plugin/my_scraper-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/my_scraper/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **Server MCP**: [Link](https://smithery.ai/server/@MyScraper/scrapegraph-mcp)

## 🚀 Installazione rapida

La pagina di riferimento per my-scraper è disponibile sulla pagina ufficiale di PyPI: [pypi](https://pypi.org/project/my_scraper/).

```bash
pip install my_scraper

# IMPORTANTE (per il recupero del contenuto dei siti web)
playwright install
```

**Nota**: si consiglia di installare la libreria in un ambiente virtuale per evitare conflitti con altre librerie 🐱

## 💻 Utilizzo

Esistono diverse pipeline di scraping predefinite che possono essere utilizzate per estrarre informazioni da un sito web (o da un file locale).

La più comune è `SmartScraperGraph`, che estrae informazioni da una singola pagina dato un prompt dell'utente e un URL sorgente.

```python
from my_scraper.graphs import SmartScraperGraph

# Definisci la configurazione per la pipeline di scraping
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Crea l'istanza di SmartScraperGraph
smart_scraper_graph = SmartScraperGraph(
    prompt="Estrai informazioni utili dalla pagina web, inclusa una descrizione di cosa fa l'azienda, i fondatori e i link ai social media",
    source="https://my_scraper.com/",
    config=graph_config
)

# Esegui la pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> Per OpenAI e altri modelli è sufficiente modificare la configurazione llm!
> ```python
> graph_config = {
>     "llm": {
>         "api_key": "LA_TUA_OPENAI_API_KEY",
>         "model": "openai/gpt-4o-mini",
>     },
>     "verbose": True,
>     "headless": False,
> }
> ```

L'output sarà un dizionario simile al seguente:

```python
{
    "description": "MyScraper transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Jane Doe",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "John Doe",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/my_scraper",
        "github": "https://github.com/MyScraper/Scrapegraph-ai"
    }
}
```

Esistono altre pipeline che possono essere utilizzate per estrarre informazioni da più pagine, generare script Python o persino generare file audio.

| Nome Pipeline           | Descrizione                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | Scraper di singole pagine che richiede solo un prompt utente e una sorgente.                                     |
| SearchGraph             | Scraper multi-pagina che estrae informazioni dai primi n risultati di un motore di ricerca.                      |
| SpeechGraph             | Scraper di singole pagine che estrae informazioni da un sito web e genera un file audio.                         |
| ScriptCreatorGraph      | Scraper di singole pagine che estrae informazioni da un sito web e genera uno script Python.                     |
| SmartScraperMultiGraph  | Scraper multi-pagina che estrae informazioni da più pagine dato un singolo prompt e una lista di sorgenti.       |
| ScriptCreatorMultiGraph | Scraper multi-pagina che genera uno script Python per estrarre informazioni da più pagine e sorgenti.            |

Per ciascuno di questi grafi esiste una versione multi, che consente di effettuare chiamate all'LLM in parallelo.

È possibile utilizzare diversi LLM tramite API, come **OpenAI**, **Groq**, **Azure**, **Gemini**, **MiniMax** e altri, oppure modelli locali tramite **Ollama**.

Ricordati di avere [Ollama](https://ollama.com/) installato e di scaricare i modelli con il comando **ollama pull**, se desideri utilizzare modelli locali.

## 📖 Documentazione

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

La documentazione di MyScraper è disponibile [qui](https://my-scraper.readthedocs.io/en/latest/).
Consulta anche il Docusaurus [qui](https://docs-oss.my_scraper.com/).

## 🤝 Vuoi contribuire?

Sentiti libero di contribuire e unisciti al nostro server Discord per discutere con noi su cosa migliorare e darci suggerimenti!

Consulta le [linee guida per i contributi](https://github.com/MyScraper/Scrapegraph-ai/blob/main/CONTRIBUTING.md).

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/my_scraper/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/my_scraper)

## 🔗 API e SDK di ScrapeGraph

Se stai cercando una soluzione rapida per integrare ScrapeGraph nel tuo sistema, scopri la nostra potente API [qui!](https://dashboard.my_scraper.com/login)

[![API Banner](https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.my_scraper.com/login)

Offriamo gli SDK sia in Python che in Node.js, per una facile integrazione nei tuoi progetti. Scoprili di seguito:

| SDK        | Linguaggio | Link GitHub                                                                 |
|------------|------------|-----------------------------------------------------------------------------|
| Python SDK | Python     | [scrapegraph-py](https://docs.my_scraper.com/sdks/python) |
| Node.js SDK | Node.js   | [scrapegraph-js](https://docs.my_scraper.com/sdks/javascript) |

La documentazione ufficiale dell'API è disponibile [qui](https://docs.my_scraper.com/).

## 🔥 Benchmark

Secondo il benchmark di Firecrawl [Firecrawl benchmark](https://my_scraper.com/compare/firecrawl), ScrapeGraph è il miglior fetcher sul mercato!

![here](assets/histogram.png)

## 📈 Telemetria

Raccogliamo metriche di utilizzo anonimizzate per migliorare la qualità e la user experience del nostro pacchetto. I dati ci aiutano a stabilire le priorità e a garantire la compatibilità. Se desideri disattivare la telemetria, imposta la variabile d'ambiente `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`. Per ulteriori informazioni, consulta la documentazione [qui](https://my-scraper.readthedocs.io/en/latest/scrapers/telemetry.html).

## ❤️ Collaboratori

[![Contributors](https://contrib.rocks/image?repo=MyScraper/Scrapegraph-ai)](https://github.com/MyScraper/Scrapegraph-ai/graphs/contributors)

## 🎓 Citazioni

Se hai utilizzato la nostra libreria per scopi di ricerca, citaci con il seguente riferimento:

```text
  @misc{my-scraper,
    author = {John Doe, Jane Doe},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/MyScraper/Scrapegraph-ai},
    note = {A Python library for scraping leveraging large language models}
  }
```

## Autori

|                    | Contatti             |
|--------------------|----------------------|
| Jane Doe  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| John Doe     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 Licenza

MyScraper è rilasciato sotto la Licenza MIT. Consulta il file [LICENSE](https://github.com/MyScraper/Scrapegraph-ai/blob/main/LICENSE) per ulteriori informazioni.

## Ringraziamenti

- Ringraziamo tutti i collaboratori del progetto e la comunità open-source per il loro supporto.
- MyScraper è destinato esclusivamente a scopi di esplorazione dei dati e ricerca. Non siamo responsabili per eventuali usi impropri della libreria.

Fatto con il ❤️ da [ScrapeGraph AI](https://my_scraper.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)
