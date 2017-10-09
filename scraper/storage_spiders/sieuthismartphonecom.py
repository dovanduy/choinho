# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='bl-product-name-info']/h1",
    'price' : "//div[@class='price_number']/span",
    'category' : "//div[@class='breadcrumbs_product_detail']/ul/li/a/span",
    'description' : "//div[@class='product_detail_Specifications']/ul/li",
    'images' : "//div[@class='bl-product-image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthismartphone.com'
allowed_domains = ['hn.sieuthismartphone.com']
start_urls = ['http://hn.sieuthismartphone.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/detail/product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]