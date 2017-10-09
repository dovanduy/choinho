# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='wapper singlewap']/div/h1[@class='title']",
    'price' : "//div[@class='rightsing']/div[@class='topleft']/p/b",
    'category' : "//p[@class='breadcrumb']/a",
    'description' : "//div[@id='more_info_block']/div[@id='description']",
    'images' : "//div[@class='image-block']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioidinhduong.vn'
allowed_domains = ['thegioidinhduong.vn']
start_urls = ['http://thegioidinhduong.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
