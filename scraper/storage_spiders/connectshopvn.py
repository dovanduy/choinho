# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-description']/div[@class='pd-name']/h1",
    'price' : "//div[@class='product-description']/div[@class='pctemp']/div",
    'category' : "//div[@class='lead_s2']/div[2]/a",
    'description' : "//div[@class='pcdetails']/div[@id='usual7']/div[@id='tab1']",
    'images' : "//div[@class='phimg']/div[@class='thumb-view']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'connectshop.vn'
allowed_domains = ['connectshop.vn']
start_urls = ['http://connectshop.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
