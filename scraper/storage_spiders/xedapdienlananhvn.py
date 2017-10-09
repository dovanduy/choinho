# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/h1",
    'price' : "//div[@class='Row Price']/div[@class='ProductPrice VariationProductPrice']",
    'category' : "",
    'description' : "//div[@class='ProcductContainer']/div[@class='ProductTabs']/div[@id='ProductDescription']",
    'images' : "//div[@class='ProductThumb']/div[@class='ProductThumbImage']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'xedapdienlananh.vn'
allowed_domains = ['xedapdienlananh.vn']
start_urls = ['http://xedapdienlananh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b\d+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]