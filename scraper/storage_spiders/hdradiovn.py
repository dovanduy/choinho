# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//p[@class='m_5']/span",
    'category' : "//div[@class='headWrap']/p[@class='breadcrumb']/a",
    'description' : "//div[@class='container']/div[@class='toogle']",
    'images' : "//img[@class='etalage_source_image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hdradio.vn'
allowed_domains = ['hdradio.vn']
start_urls = ['http://hdradio.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|\?page=\d+$)']), 'parse_item_and_links'),
]
