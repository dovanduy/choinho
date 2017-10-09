# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='jshop-titleheading']",
    'price' : "//div[@class='prod_price']/span[@id='block_price']",
    'category' : "//li[@class='lofitem1 ice-current lofactive']/a/span",
    'description' : "//div[@class='product-detail']/div[@class='jshop_prod_description']/table[@class='specTable']",
    'images' : "//div[@class='product-image']/div[@class='product-image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'memoryzone.com.vn'
allowed_domains = ['memoryzone.com.vn']
start_urls = ['http://memoryzone.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(allow=['']), 'parse_item'),
    #Rule(LinkExtractor(allow=['']), 'parse'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item_and_links'),
]
