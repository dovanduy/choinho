# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='jshop productfull']//h1",
    'price' : "//span[@id='block_price']",
    'category' : "",
    'description' : "//div[@class='jshop_prod_description']",
    'images' : "//td[@class='image_middle']/span/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'phanphoilaptop.com'
allowed_domains = ['phanphoilaptop.com']
start_urls = ['http://www.phanphoilaptop.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
