# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tool_product']/p[1]/label[2]",
    'price' : "//div[@class='tool_product']/p[3]/label[2]",
    'category' : "//div[@class='breadcum']/a",
    'description' : "//table[@class='detail_product']",
    'images' : "//div[@class='full_image']/a[@class='lightbox']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'calculatorcentre.com'
allowed_domains = ['calculatorcentre.com']
start_urls = ['http://calculatorcentre.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi_tiet_sp/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/ds_san_pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
