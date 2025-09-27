from eventregistry import *
from datetime import datetime, timedelta

# initialize Event Registry with your API key
er = EventRegistry(apiKey="fa62084d-9c12-4a1d-865a-2ddafd17aa6a")
europeUri = er.getLocationUri("Europe")
today = datetime.utcnow()
last_7_days = today - timedelta(days=7)
CATEGORIES = {
    "technology": "dmoz/Computers",
    "sports": "dmoz/Sports",
    "business": "dmoz/Business",
    "culture": "dmoz/Arts",
    "politics": "dmoz/Society/Politics",
    "health": "dmoz/Health",
    "science": "dmoz/Science"
}

def fetch_articles(category="technology", keywords=None, days=7, lang="eng", max_items=20, sources=None):
    today = datetime.utcnow()
    start_date = today - timedelta(days=days)

    q = QueryArticlesIter(
        categoryUri=CATEGORIES.get(category),
        keywords=QueryItems.OR([keywords]) if keywords else None,
        keywordsLoc="title",
        lang=lang,
        dataType=["news"],
        dateStart=start_date.strftime("%Y-%m-%d"),
        dateEnd=today.strftime("%Y-%m-%d"),
        sourceLocationUri=europeUri,
        sourceUri=sources 
    )
    
    results = []
    for art in q.execQuery(er, sortBy="date", maxItems=max_items):
        results.append({
            "title": art.get("title"),
            "url": art.get("url"),
            "body": art.get("body"),
            "source": art.get("source", {}).get("title"),
            "date": art.get("dateTime")
        })
    return results
