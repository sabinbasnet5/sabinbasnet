import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"	    
    
    start_urls = ["http://www.takeo.ai/"]

    def parse(self, response):
        # Extract the page title
        title = response.css('title::text').get()
        # Print the title
        self.log(f'Title: {title}')
