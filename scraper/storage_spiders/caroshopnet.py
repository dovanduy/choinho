# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='post-header']/h1[@id='post-title']",
    'price' : "",
    'category' : "",
    'description' : "//div[@class='post-content']/h1",
    'images' : "//div[@class='post-content']/p/a/@href | //div[@class='post-content']/div/a/@href | //div[@class='post-content']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'caroshop.net'
allowed_domains = ['caroshop.net']
start_urls = ['http://www.caroshop.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
