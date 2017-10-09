# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title']/h1",
    'price' : "//strong[@class='sell_price']/span[@class='uc-price']",
    'category' : "//div[@class='breadcrumb']/span/a/span",
    'description' : "//div[@class='productBody']/div[@class='content']",
    'images' : "//div[@id='images_preview']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthimay.net.vn'
allowed_domains = ['sieuthimay.net.vn']
start_urls = ['http://sieuthimay.net.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
