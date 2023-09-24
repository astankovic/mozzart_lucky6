from web_app import app
from scraper.spiders.my_spider import scrape_url

@app.route('/scrape/<path:url>')
def scrape_endpoint(url):
    data = scrape_url(url)
    return data

