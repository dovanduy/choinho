# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_title entry-title']",
    'price' : "//p[@class='price']/ins/span[@class='amount']",
    'category' : "//ul[@class='breadcrumb']/li/a/span",
    'description' : "//div[@id='tab-description']",
    'images' : "//img[@class='zoom']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'mysticare.vn'
allowed_domains = ['mysticare.vn']
start_urls = ['http://mysticare.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[^(san-pham)]+'], deny=['tag','anwers','gioi-thieu','tin-tuc']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
