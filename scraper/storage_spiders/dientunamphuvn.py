# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='fl pro-info']/h1[@class='pro-name']",
    'price' : "//div[@class='fl pro-info']/p/span[@class='price']",
    'category' : "//div[@class='breacrumb']/a",
    'description' : "//div[@class='block-main']/div[@id='tabs1']/div[@id='tab1']",
    'images' : "//div[@class='fl pro-img']/div[@id='img_large_np']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dientunamphu.vn'
allowed_domains = ['dientunamphu.vn']
start_urls = ['http://dientunamphu.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]