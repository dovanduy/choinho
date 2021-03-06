# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table[@class='mainTable']/tbody/tr/td/font[@class='text_news_content_new']",
    'price' : "//table[@class='mainTable']/tbody/tr[2]/td/center/b",
    'category' : "table[@class='mainTable']/tbody/tr[3]/td",
    'description' : "//tr[3]/td/table[@class='mainTable']/tbody/tr[3]/td",
    'images' : "//table[@class='mainTable']/tbody/tr/td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thienantech.com'
allowed_domains = ['thienantech.com']
start_urls = ['http://www.thienantech.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
