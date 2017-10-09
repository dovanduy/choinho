# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='deal-buy']/p[@class='deal-price']/strong",
    'category' : "",
    'description' : "//div[@class='box-content cf']/div[@class='main']",
    'images' : "//div[@class='deal-buy-cover-img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vndeal.net'
allowed_domains = ['vndeal.net']
start_urls = ['http://vndeal.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$'], deny=['/i\d+-[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/i\d+-[a-zA-Z0-9-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
