# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info_summary']/div[@class='name_product']",
    'price' : "//div[@class='info_summary']/div[@class='price']/b",
    'category' : "//div[@class='location']/a",
    'description' : "//div[@class='detail']/div[@id='info_detail']",
    'images' : "//div[@class='overview']/div[@class='img_product']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'shopgauyeu.vn'
allowed_domains = ['shopgauyeu.vn']
start_urls = ['http://shopgauyeu.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
