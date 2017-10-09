# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='summary entry-summary']/h1",
    'price' : "//div[@class='summary entry-summary']/div/p/del/span[@class='amount'] | //div[@class='summary entry-summary']/div/p[@class='price']/ins/span[@class='amount'] | //div[@class='summary entry-summary']/div/p[@class='price']/ins",
    'category' : "",
    'description' : "//div[@class='woocommerce-tabs']/div[@id='tab-description']",
    'images' : "//div[@class='images']/a/img/@src | //div[@class='images']/div[@class='thumbnails']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'chaienshop.com'
allowed_domains = ['chaienshop.com']
start_urls = ['http://chaienshop.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/?product=']), 'parse_item'),
    Rule(LinkExtractor(allow=['/?product_cat=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
