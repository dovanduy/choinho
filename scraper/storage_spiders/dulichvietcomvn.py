# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='headline_area']/strong/h1[@class='entry-title']",
    'price' : "//div[@class='format_text entry-content']/strong[@class='travel_price']",
    'category' : "//div[@id='travelbreadcrumbs']",
    'description' : "///div[contains(@id,'tabs')]",
    'images' : "//img[@class='thumb alignleft remove_bottom_margin frame']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dulichviet.com.vn'
allowed_domains = ['dulichviet.com.vn']
start_urls = ['http://dulichviet.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
