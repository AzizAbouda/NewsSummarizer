import streamlit as st
from functions.news_api import fetch_articles
from functions.summarizer import summarize_long_text
from eventregistry import QueryItems

st.set_page_config(page_title="Personalized News Summarizer", layout="wide")
st.title("📰 Personalized News Summarizer")

# Available categories (must match your CATEGORIES in news_api.py)
CATEGORIES = ["technology", "sports", "business", "culture", "politics", "health", "science"]

# UI controls
category = st.selectbox("Choose a category:", CATEGORIES, index=0)
keywords = st.text_input("Enter keywords (optional):", "")
sources = QueryItems.OR([
    "bbc.co.uk", "cnn.com", "reuters.com", "apnews.com", "nytimes.com",
    "theguardian.com", "washingtonpost.com", "aljazeera.com", "bloomberg.com",
    "euronews.com", "dw.com", "lemonde.fr", "spiegel.de", "ft.com",
    "forbes.com", "wsj.com", "economist.com"
])
if st.button("Fetch & Summarize"):
    with st.spinner("Fetching latest articles..."):
        articles = fetch_articles(category=category, keywords=keywords,sources=sources, max_items=5)
    
    if not articles:
        st.warning("No articles found.")
    else:
        for article in articles:
            st.subheader(article['title'])
            st.caption(f"{article.get('source')} — {article.get('date')}")
            
            # Use body if available, fallback to title
            content = article.get("body") or article.get("title") or ""
            if content.strip():
                summary = summarize_long_text(content)
                st.write(summary)
            else:
                st.info("No content available to summarize.")
            
            st.markdown(f"[Read more]({article['url']})")
            st.markdown("---")
