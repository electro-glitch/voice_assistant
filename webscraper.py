import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals
import re

class SimpleSpider(scrapy.Spider):
    name = "simple_spider"

    def __init__(self, url, query, *args, **kwargs):
        super(SimpleSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.query = query.lower()  # Convert query to lowercase for case-insensitive matching
        self.results = []

    def parse(self, response):
        # Extract all visible text from the page
        all_text = " ".join(response.css("body *::text").getall())
        all_text = re.sub(r"\s+", " ", all_text.strip())  # Clean up extra whitespace

        # Search for the query string in the extracted text
        if self.query in all_text.lower():
            # Find all matching sentences or phrases containing the query
            sentences = re.findall(rf"([^.]*?\b{re.escape(self.query)}\b.*?\.)", all_text, re.IGNORECASE)
            self.results.append(" ".join(sentences))

# Function to run the spider and return the results
def run_scraper(url, query):
    results = []

    def collect_results(signal, sender, item, response, spider):
        results.extend(spider.results)

    process = CrawlerProcess(settings={
        "LOG_LEVEL": "ERROR"  # Suppress logs for cleaner output
    })

    # Connect to the spider_closed signal to collect results
    dispatcher.connect(collect_results, signal=signals.spider_closed)

    # Schedule the spider
    process.crawl(SimpleSpider, url=url, query=query)
    process.start()  # Start the crawling process

    return results[0] if results else "No relevant text found."
