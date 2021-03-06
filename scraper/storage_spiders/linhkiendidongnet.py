# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product-title']/span",
    'price' : "//h3[@class='product-price']/span",
    'category' : "//h2[@class='product-category-title']/a",
    'description' : "//div[@class='product-info-tab']/div[@class='tab-content']//p",
    'images' : "//div[@class='fotorama']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'linhkiendidong.net'
allowed_domains = ['linhkiendidong.net']
start_urls = ['http://linhkiendidong.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['san-pham/\d+/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/categories/\d+/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
