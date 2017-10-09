# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='block-detail-production']/div[@class='block-right']/h1[@class='title-name']",
    'price' : "//p/span[@class='gia_chinh']/b | //span[@class='gia_chinh']",
    'category' : "//ul[@class='list_items_link']/li/a",
    'description' : "//div[@class='info-left']/div[@class='description-topic']/p",
    'images' : "//div[@class='pic-big']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'muathuoctot.com'
allowed_domains = ['muathuoctot.com']
start_urls = ['http://muathuoctot.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.cat']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
