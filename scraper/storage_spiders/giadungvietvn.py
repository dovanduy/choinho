# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='single-content-1']/div[@class='info floatr']/header/h1[@class='title']",
    'price' : "//div[@class='col11 floatl']/p[@class='price']/span",
    'category' : "//div[@id='breadcrumb']/a",
    'description' : "//div[@id='content-detail-info']/p",
    'images' : "//div[@id='single-content-1']/div[@id='product-images']//img/@src | //meta[@property='og:image']/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'giadungviet.vn'
allowed_domains = ['giadungviet.vn']
start_urls = ['http://giadungviet.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/.*\d+.*/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
