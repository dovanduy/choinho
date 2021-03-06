# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-shop']/div[@class='product-name']/h1",
    'price' : "//div[@class='product-shop']/div[@class='price-box']/span/span[@class='price'] | //div[@class='price-box']/p[@class='special-price']/span[@id='product-price-328']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='description-content'] | //div[@class='box-collateral box-additional']",
    'images' : "//div[@class='product-img-box']/div[@class='more-views']/ul/li/a/@href|//p[@class='product-image']/div[@id='wrap']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'donghosaigon.vn'
allowed_domains = ['donghosaigon.vn']
start_urls = ['http://www.donghosaigon.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
