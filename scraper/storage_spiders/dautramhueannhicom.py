# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//form[@id='buy_product']/div[@class='price-num']/div[@class='price']/span[@class='price-new']",
    'category' : "",
    'description' : "//section[@id='product-tab']/ul[@class='tab']",
    'images' : "//img[@id='main_img']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dautramhueannhi.com'
allowed_domains = ['dautramhueannhi.com']
start_urls = ['http://dautramhueannhi.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['dautramhueannhi\.com$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]