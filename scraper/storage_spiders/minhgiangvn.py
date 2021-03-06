# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='block-single']/h1[@class='single-title']",
    'price' : "//div[@class='block-single']/p[@class='price']",
    'category' : "//p[@class='block-breadcrumb']/a",
    'description' : "",
    'images' : "//div[@class='block-single']/img/@src | //div[@class='block-single']/p/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'minhgiang.vn'
allowed_domains = ['minhgiang.vn']
start_urls = ['http://minhgiang.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
