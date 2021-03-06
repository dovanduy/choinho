# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='page-noneback']/h1",
    'price' : "//div[@class='col-md-12 col-sm-12 col-xs-12']//div[@class='priceInfo']/span[@class='price']",
    'category' : "//a[@class='bread-crumb-item']",
    'description' : "//div[@id='hcv-post-content']/div[@class='panel entry-content']/p",
    'images' : "//div[@id='product-slider']/ul[@class='slides']/li/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'vinakaraoke.vn'
allowed_domains = ['vinakaraoke.vn']
start_urls = ['http://vinakaraoke.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d+.*$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+($|/\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
