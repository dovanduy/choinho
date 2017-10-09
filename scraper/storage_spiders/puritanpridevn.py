# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='left_']/div[3]/h2",
    'price' : "//div[@class='specifications']/div[5]/ul/li/form/label/p[2]/span",
    'category' : "//div[@id='left_']/div[1]/a",
    'description' : "//div[@class='tabcontentstyle']/div[@id='tab2']/div[@id='stcpDiv']",
    'images' : "//div[@class='clearfix chitietsp']/img/@data-large",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'puritanpride.vn'
allowed_domains = ['puritanpride.vn']
start_urls = ['http://www.puritanpride.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/detail-\d+-[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/catergories3-\d+-[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
