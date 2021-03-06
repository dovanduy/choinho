# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='col_center']/div[@id='cenTop']/h1",
    'price' : "//form[@id='frmproduct']/div[@id='viewRight']/li[4]",
    'category' : "//div[@id='col_center']/div[@id='cenTop']/ul/a",
    'description' : "//form[@id='frmproduct']/div[@id='viewRight']/p",
    'images' : "//form[@id='frmproduct']/div[@id='viewLeft']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioidentrangtri.com'
allowed_domains = ['thegioidentrangtri.com']
start_urls = ['http://thegioidentrangtri.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-p+\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-c+\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
