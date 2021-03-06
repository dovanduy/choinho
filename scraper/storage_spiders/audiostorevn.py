# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_info']/div[@class='pd-name']/h1[@id='config_name']",
    'price' : "//div[@class='product_info']/div[@class='pctemp']/span[@id='config_price']",
    'category' : "//div[@class='main']/div[@class='lead_sub']/a",
    'description' : "//div[@class='pcdetails']/div[@id='usual7']/div[@id='tab1']",
    'images' : "//div/@data-src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'audiostore.vn'
allowed_domains = ['audiostore.vn']
start_urls = ['http://audiostore.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/'], deny=['sort=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
