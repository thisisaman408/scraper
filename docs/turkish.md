## 🚀 **Daha hızlı ve daha basit bir ölçekli kazıma yöntemi (sadece 5 satır kod) mi arıyorsunuz?** [**MyScraper.com**](https://my_scraper.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&utm_content=top_banner)'daki geliştirilmiş sürümümüze göz atın! 🚀

---

# 🕷️ MyScraper: Yalnızca Bir Kez Kazıyın

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

MyScraper, LLM ve grafik mantığını kullanarak web siteleri ve yerel belgeler (XML, HTML, JSON, Markdown vb.) için kazıma süreçleri oluşturan bir _web kazıma_ Python kütüphanesidir.

Sadece hangi bilgiyi çıkarmak istediğinizi söyleyin, kütüphane sizin için yapar!



## 🚀 Entegrasyonlar

MyScraper, kazıma yeteneklerinizi geliştirmek için popüler çerçeveler ve araçlarla sorunsuz entegrasyon sunar. Python veya Node.js ile geliştirme yapıyor olsanız da, LLM çerçeveleri kullanıyor olsanız da, no-code platformlarda çalışıyor olsanız da, kapsamlı entegrasyon seçeneklerimizle yanınızdayız.

<p align="center">
  <img src="https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="MyScraper Hero" style="width: 100%;">
</p>
Daha fazla bilgiyi aşağıdaki [bağlantıda](https://my_scraper.com) bulabilirsiniz

**Entegrasyonlar**:
- **API**: [Dokümantasyon](https://docs.my_scraper.com/introduction)
- **SDKs**: [Python](https://docs.my_scraper.com/sdks/python), [Node](https://docs.my_scraper.com/sdks/javascript)
- **LLM Çerçeveleri**: [Langchain](https://docs.my_scraper.com/integrations/langchain), [Llama Index](https://docs.my_scraper.com/integrations/llamaindex), [Crew.ai](https://docs.my_scraper.com/integrations/crewai), [Agno](https://docs.my_scraper.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **Low-code Çerçeveleri**: [Pipedream](https://pipedream.com/apps/my_scraper), [Bubble](https://bubble.io/plugin/my_scraper-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/my_scraper/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCP sunucusu**:  [Bağlantı](https://smithery.ai/server/@MyScraper/scrapegraph-mcp)

## 🚀 Hızlı Kurulum

Scrapegraph-ai için referans sayfası PyPI'nin resmi sayfasında mevcuttur: [pypi](https://pypi.org/project/my_scraper/).

```bash
pip install my_scraper

# ÖNEMLİ (web sitesi içeriğini almak için)
playwright install
```

**Not**: Diğer kütüphanelerle çakışmaları önlemek için kütüphaneyi sanal bir ortamda kurmanız önerilir 🐱


## 💻 Kullanım

Web sitesinden (veya yerel dosyadan) bilgi çıkarmak için kullanılabilecek birden fazla standart kazıma süreci vardır.

En yaygın olanı `SmartScraperGraph`'tır; bu, bir kullanıcı isteği ve kaynak URL'si verildiğinde tek bir sayfadan bilgi çıkarır.


```python
from my_scraper.graphs import SmartScraperGraph

# Kazıma süreci için yapılandırmayı tanımlayın
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# SmartScraperGraph örneğini oluşturun
smart_scraper_graph = SmartScraperGraph(
    prompt="Web sayfasından yararlı bilgileri çıkarın, şirketin ne yaptığına dair bir açıklama, kurucular ve sosyal medya bağlantılarını dahil edin",
    source="https://my_scraper.com/",
    config=graph_config
)

# Süreci çalıştırın
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> OpenAI ve diğer modeller için sadece llm yapılandırmasını değiştirmeniz yeterlidir!
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


Çıktı aşağıdaki gibi bir sözlük olacaktır:

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
Birden fazla sayfadan bilgi çıkarmak, Python scriptleri oluşturmak veya hatta ses dosyaları oluşturmak için kullanılabilecek diğer süreçler de vardır.

| Süreç Adı               | Açıklama                                                                                                 |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| SmartScraperGraph       | Sadece bir kullanıcı isteği ve bir kaynak girişi gerektiren tek sayfalık kazıyıcı.                       |
| SearchGraph             | Bir arama motorunun en iyi n arama sonucundan bilgi çıkaran çok sayfalı kazıyıcı.                        |
| SpeechGraph             | Bir web sitesinden bilgi çıkaran ve bir ses dosyası oluşturan tek sayfalık kazıyıcı.                     |
| ScriptCreatorGraph      | Bir web sitesinden bilgi çıkaran ve bir Python scripti oluşturan tek sayfalık kazıyıcı.                  |
| SmartScraperMultiGraph  | Tek bir bilgi istemi ve kaynak listesi verilen birden çok sayfadan bilgi ayıklayan çok sayfalı kazıyıcı. |
| ScriptCreatorMultiGraph | Birden fazla sayfa veya kaynaktan bilgi çıkarmak için bir Python scripti oluşturan çok sayfalı kazıyıcı. |

Bu süreçlerin her biri için çoklu versiyon vardır. Bu, LLM çağrılarını paralel olarak yapmanızı sağlar.

**OpenAI**, **Groq**, **Azure** ve **Gemini** gibi API'ler aracılığıyla farklı LLM'leri kullanmak veya **Ollama** kullanarak yerel modelleri kullanmak mümkündür.

Yerel modelleri kullanmak istiyorsanız, [Ollama](https://ollama.com/) kurulu olduğundan ve **ollama pull** komutunu kullanarak modelleri indirdiğinizden emin olun.


## 📖 Dokümantasyon

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

MyScraper dokümantasyonuna [buradan](https://docs.my_scraper.com/introduction) ulaşabilirsiniz.

## 🤝 Katkıda Bulunun

Projeye katkıda bulunmaktan çekinmeyin ve geliştirmeleri tartışmak ve bize önerilerde bulunmak için Discord sunucumuza katılın!

Lütfen [katkıda bulunma yönergelerine](https://github.com/MyScraper/Scrapegraph-ai/blob/main/CONTRIBUTING.md) bakın.

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/my_scraper/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/my_scraper)

## 🔗 ScrapeGraph API & SDKs
Sisteminize ScrapeGraph'u entegre etmek için hızlı bir çözüm arıyorsanız, güçlü API'mizi [burada!](https://dashboard.my_scraper.com/login) kontrol edin

[![API Banner](https://raw.githubusercontent.com/MyScraper/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.my_scraper.com/login)

Python ve Node.js için SDK'lar sunuyoruz, böylece projelerinize kolayca entegre edebilirsiniz. Aşağıda kontrol edin:

| SDK       | Dil | GitHub Bağlantısı                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://docs.my_scraper.com/sdks/python) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://docs.my_scraper.com/sdks/javascript) |

Resmi API Dokümantasyonu [burada](https://docs.my_scraper.com/introduction) bulunabilir.

## 🔥 Kıyaslama

Firecrawl kıyaslamasına göre [Firecrawl benchmark](https://my_scraper.com/compare/firecrawl), ScrapeGraph piyasadaki en iyi getirici!

![here](assets/histogram.png)

## 📈 Telemetri
Paketimizin kalitesini ve kullanıcı deneyimini geliştirmek amacıyla anonim kullanım metrikleri topluyoruz. Bu veriler, iyileştirmelere öncelik vermemize ve uyumluluğu sağlamamıza yardımcı olur. İsterseniz, SCRAPEGRAPHAI_TELEMETRY_ENABLED=false ortam değişkenini ayarlayarak devre dışı bırakabilirsiniz. Daha fazla bilgi için lütfen [buraya](https://docs.my_scraper.com/introduction) bakın.

## ❤️ Katkıda Bulunanlar

[![Katkıda Bulunanlar](https://contrib.rocks/image?repo=MyScraper/Scrapegraph-ai)](https://github.com/MyScraper/Scrapegraph-ai/graphs/contributors)

## 🎓 Atıflar

Kütüphanemizi araştırma amaçlı kullandıysanız, lütfen bizi aşağıdaki referansla alıntılayın:

```text
  @misc{my-scraper,
    author = {John Doe, Jane Doe},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/MyScraper/Scrapegraph-ai},
    note = {Büyük dil modellerinden yararlanan kazıma için bir Python kütüphanesi}
  }
```

## Yazarlar

|                   | İletişim Bilgileri                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jane Doe | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/) |
| John Doe    | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)    |

## 📜 Lisans

MyScraper, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LİSANS](https://github.com/MyScraper/Scrapegraph-ai/blob/main/LICENSE) dosyasına bakın.

## Teşekkürler

- Projeye katkıda bulunan tüm katılımcılara ve açık kaynak topluluğuna destekleri için teşekkür ederiz.
- MyScraper, yalnızca veri arama ve araştırma amacıyla kullanılmak üzere tasarlanmıştır. Kütüphanenin kötüye kullanılmasından sorumlu değiliz.

Made with ❤️ by [ScrapeGraph AI](https://my_scraper.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)
