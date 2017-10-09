# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='cf']/div/div/h1[@class='thread-details-title']",
    'price' : "//div[@class='cf']/div/div[@class='redcolor bold thread-details-giamoi']/span",
    'category' : "//div[@id='oi_main']/div[@id='rME']/div[@class='thread-details thread-details-tohome']/a",
    'description' : "//div/div[@class='thread-details']/div/div[@id='thread_content_pack']",
    'images' : "//div/div[@class='product-thumb']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'lahuka.vn'
allowed_domains = ['lahuka.vn']
start_urls = ['http://lahuka.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/muanhom+-\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[fs]+id+-\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
