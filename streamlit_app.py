import streamlit as st
import os
import json

# Ensure playwright browser is installed for Streamlit Cloud
os.system("playwright install chromium")

from my_scraper.graphs import SmartScraperGraph

st.set_page_config(page_title="MyScraper Dashboard", page_icon="✨")

st.title("✨ MyScraper Web Dashboard")
st.markdown("Extract structured data from any website using AI!")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    model = st.selectbox("Model", ["groq/llama-3.3-70b-versatile", "groq/llama-3.1-8b-instant"])
    
# Main inputs
url = st.text_input("Website URL", placeholder="https://news.ycombinator.com/")
prompt = st.text_area("Extraction Prompt", placeholder="Extract the top 5 articles from the page with their details.")

if st.button("🚀 Scrape Website"):
    if not api_key:
        st.error("Please provide a Groq API key in the sidebar!")
    elif not url or not prompt:
        st.error("Please provide both a URL and a prompt.")
    else:
        with st.spinner("Scraping and analyzing website..."):
            try:
                graph_config = {
                    "llm": {
                        "api_key": api_key,
                        "model": model, 
                    },
                    "verbose": False,
                    "headless": True,
                }
                
                scraper = SmartScraperGraph(
                    prompt=prompt,
                    source=url,
                    config=graph_config
                )
                
                result = scraper.run()
                
                st.success("Scraping successful!")
                st.subheader("Data Extracted:")
                st.json(result)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
