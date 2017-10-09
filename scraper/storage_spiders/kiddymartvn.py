# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='product-quick-view']/div[@class='left-info']/div[@class='price-box']/span/span",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='box-collateral box-description']",
    'images' : "//img[@id='zoom_03']/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kiddymart.vn'
allowed_domains = ['kiddymart.vn']
start_urls = ['http://kiddymart.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
