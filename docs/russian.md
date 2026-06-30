## 🚀 **Ищете еще более быстрый и простой способ масштабного скрейпинга (всего 5 строк кода)?** Ознакомьтесь с нашей улучшенной версией на [**MyScraper.com**](https://my_scraper.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&utm_content=top_banner)! 🚀

---

# 🕷️ MyScraper: Вы скрейпите только один раз

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

MyScraper - это библиотека для веб-скрейпинга на Python, которая использует LLM и прямую графовую логику для создания скрейпинговых пайплайнов для веб-сайтов и локальных документов (XML, HTML, JSON, Markdown и т.д.).

Просто укажите, какую информацию вы хотите извлечь, и библиотека сделает это за вас!



## 🚀 Интеграции

MyScraper предлагает бесшовную интеграцию с популярными фреймворками и инструментами для улучшения ваших возможностей скрейпинга. Независимо от того, создаете ли вы приложения на Python или Node.js, используете ли LLM-фреймворки или работаете с платформами без кода, мы предоставляем комплексные варианты интеграции.

<p align="center">
  <img src="https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="MyScraper Hero" style="width: 100%;">
</p>
Вы можете найти больше информации по следующей [ссылке](https://my_scraper.com)

**Интеграции**:
- **API**: [Документация](https://docs.my_scraper.com/introduction)
- **SDKs**: [Python](https://docs.my_scraper.com/sdks/python), [Node](https://docs.my_scraper.com/sdks/javascript)
- **LLM Фреймворки**: [Langchain](https://docs.my_scraper.com/integrations/langchain), [Llama Index](https://docs.my_scraper.com/integrations/llamaindex), [Crew.ai](https://docs.my_scraper.com/integrations/crewai), [Agno](https://docs.my_scraper.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **Low-code Фреймворки**: [Pipedream](https://pipedream.com/apps/my_scraper), [Bubble](https://bubble.io/plugin/my_scraper-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/my_scraper/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCP сервер**:  [Ссылка](https://smithery.ai/server/@MyScraper/scrapegraph-mcp)

## 🚀 Быстрая установка

Референсная страница для Scrapegraph-ai доступна на официальной странице PyPI: [pypi](https://pypi.org/project/my_scraper/).

```bash
pip install my_scraper

# ВАЖНО (для получения содержимого веб-сайтов)
playwright install
```

**Примечание**: рекомендуется устанавливать библиотеку в виртуальную среду, чтобы избежать конфликтов с другими библиотеками 🐱


## 💻 Использование
Существует несколько стандартных скрейпинговых пайплайнов, которые можно использовать для извлечения информации с веб-сайта (или локального файла).

Наиболее распространенным является `SmartScraperGraph`, который извлекает информацию с одной страницы при наличии пользовательского запроса и исходного URL.


```python
from my_scraper.graphs import SmartScraperGraph

# Определите конфигурацию для скрейпингового пайплайна
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Создайте экземпляр SmartScraperGraph
smart_scraper_graph = SmartScraperGraph(
    prompt="Извлеките полезную информацию с веб-страницы, включая описание деятельности компании, основателей и ссылки на социальные сети",
    source="https://my_scraper.com/",
    config=graph_config
)

# Запустите пайплайн
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> Для OpenAI и других моделей вам просто нужно изменить конфигурацию llm!
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


Выходные данные будут представлять собой словарь, например:

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
Существуют другие пайплайны, которые можно использовать для извлечения информации с нескольких страниц, генерации Python-скриптов или даже генерации аудиофайлов.

| Название пайплайна           | Описание                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | Скрейпер одной страницы, которому требуется только пользовательский запрос и источник ввода.                                           |
| SearchGraph             | Многопользовательский скрейпер, который извлекает информацию из топ n результатов поиска поисковой системы.                  |
| SpeechGraph             | Скрейпер одной страницы, который извлекает информацию с веб-сайта и генерирует аудиофайл.                       |
| ScriptCreatorGraph      | Скрейпер одной страницы, который извлекает информацию с веб-сайта и генерирует Python-скрипт.                     |
| SmartScraperMultiGraph  | Многопользовательский скрейпер, который извлекает информацию с нескольких страниц при наличии одного запроса и списка источников.    |
| ScriptCreatorMultiGraph | Многопользовательский скрейпер, который генерирует Python-скрипт для извлечения информации с нескольких страниц и источников.     |

Для каждого из этих графов существует мульти-версия. Это позволяет выполнять вызовы LLM параллельно.

Можно использовать различные LLM через API, такие как **OpenAI**, **Groq**, **Azure** и **Gemini**, или локальные модели, используя **Ollama**.

Не забудьте установить [Ollama](https://ollama.com/) и загрузить модели, используя команду **ollama pull**, если вы хотите использовать локальные модели.


## 📖 Документация

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

Документация для MyScraper доступна [здесь](https://docs.my_scraper.com/introduction).

## 🤝 Участие

Не стесняйтесь вносить свой вклад и присоединяйтесь к нашему серверу Discord, чтобы обсудить с нами улучшения и дать нам предложения!

Пожалуйста, ознакомьтесь с [руководством по участию](https://github.com/MyScraper/Scrapegraph-ai/blob/main/CONTRIBUTING.md).

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/my_scraper/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/my_scraper)

## 🔗 ScrapeGraph API & SDKs
Если вы ищете быстрое решение для интеграции ScrapeGraph в вашу систему, ознакомьтесь с нашим мощным API [здесь!](https://dashboard.my_scraper.com/login)

[![API Banner](https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.my_scraper.com/login)

Мы предлагаем SDK для Python и Node.js, что упрощает интеграцию в ваши проекты. Ознакомьтесь с ними ниже:

| SDK       | Язык | GitHub Ссылка                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://docs.my_scraper.com/sdks/python) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://docs.my_scraper.com/sdks/javascript) |

Официальная документация API доступна [здесь](https://docs.my_scraper.com/introduction).

## 🔥 Бенчмарк

Согласно бенчмарку Firecrawl [Firecrawl benchmark](https://my_scraper.com/compare/firecrawl), ScrapeGraph является лучшим фетчером на рынке!

![here](assets/histogram.png)

## 📈 Телеметрия
Мы собираем анонимные метрики использования для повышения качества нашего пакета и пользовательского опыта. Данные помогают нам определять приоритеты улучшений и обеспечивать совместимость. Если вы хотите отказаться, установите переменную окружения SCRAPEGRAPHAI_TELEMETRY_ENABLED=false. Для получения дополнительной информации обратитесь к документации [здесь](https://docs.my_scraper.com/introduction).

## ❤️ Разработчики программного обеспечения

[![Contributors](https://contrib.rocks/image?repo=MyScraper/Scrapegraph-ai)](https://github.com/MyScraper/Scrapegraph-ai/graphs/contributors)

## 🎓 Цитаты

Если вы использовали нашу библиотеку для научных исследований, пожалуйста, укажите нас в следующем виде:

```text
  @misc{my-scraper,
    author = {John Doe, Jane Doe},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/MyScraper/Scrapegraph-ai},
    note = {Библиотека на Python для скрейпинга с использованием больших языковых моделей}
  }
```

## Авторы

|                    | Контактная информация         |
|--------------------|----------------------|
| Jane Doe  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| John Doe     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 Лицензия

MyScraper лицензирован под MIT License. Подробнее см. в файле [LICENSE](https://github.com/MyScraper/Scrapegraph-ai/blob/main/LICENSE).

## Благодарности

- Мы хотели бы поблагодарить всех участников проекта и сообщество с открытым исходным кодом за их поддержку.
- MyScraper предназначен только для исследования данных и научных целей. Мы не несем ответственности за неправильное использование библиотеки.

Made with ❤️ by [ScrapeGraph AI](https://my_scraper.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)
