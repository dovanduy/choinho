# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='product-info']/div[@class='right']/h1",
    'price' : "//div[@id='content']/div[@class='product-info']/div[@class='right']/div[@class='price']",
    'category' : "//div[@id='container']/div[@id='content']/div[@class='breadcrumb']/a",
    'description' : "//table[@id='TblProdForkPromo']//tr/td[@class='contenttd']",
    'images' : "//div[@class='image']/a[@class='jqzoom']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hangxachtayusa.com.vn'
allowed_domains = ['hangxachtayusa.com.vn']
start_urls = ['http://hangxachtayusa.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['route=product/product']), 'parse_item'),
    Rule(LinkExtractor(allow=['route=product/category']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
