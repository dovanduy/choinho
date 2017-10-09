# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productTitle']/h1",
    'price' : "//div[@class='productTitle']/h2",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='productRelative']/ul/li/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'elise.com.vn'
allowed_domains = ['elise.com.vn']
start_urls = ['http://elise.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+p+\d+c+\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.htm']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
