# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='description']/h2",
    'price' : "//div[@class='price']/span[@class='price-first']",
    'category' : "",
    'description' : "//div[@id='tab-description']",
    'images' : "//div[@class='image a_bossthemes']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tngfashion.vn'
allowed_domains = ['tngfashion.vn']
start_urls = ['http://www.tngfashion.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
