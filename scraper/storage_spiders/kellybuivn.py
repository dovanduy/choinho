# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1",
    'price' : "//span[@class='price price-new'] | //div[@class='product-price']/span[@class='price price-new']",
    'category' : "",
    'description' : "//div[@class='product-info']/div[@class='product-detail']",
    'images' : "//div[@class='image-curr']/img[@class='zoomImg']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kellybui.vn'
allowed_domains = ['kellybui.vn']
start_urls = ['http://kellybui.vn/shop/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['route=product/product']), 'parse_item'),
    Rule(LinkExtractor(allow = ['route=product/category']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]