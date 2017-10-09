# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='price-block']/div[@class='price-box']/p[@class='special-price']/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='product-collateral wow bounceInUp animated animated']/div[@class='tab-content']",
    'images' : "//div[@class='large-image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//p[@class='availability in-stock pull-right']/span",
    'guarantee' : "",
    'promotion' : ""
}
name = 'mexitrum.com.vn'
allowed_domains = ['mexitrum.com.vn']
start_urls = ['http://mexitrum.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]
