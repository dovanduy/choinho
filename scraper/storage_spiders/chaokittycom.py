# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product']/h3[@class='product_title']",
    'price' : "//div[@class='item']/div[@class='img']/span[@class='product-price']",
    'category' : "",
    'description' : "//div[@class='product']/table//tr/td/div/p",
    'images' : "//div[@class='product']/table//tr/td/div[@class='item']/div[@class='img']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'chaokitty.com'
allowed_domains = ['chaokitty.com']
start_urls = ['http://chaokitty.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
