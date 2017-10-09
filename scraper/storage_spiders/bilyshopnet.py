# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='sanphamCenter']/table//tr/td/table//tr[1]/td[3]",
    'price' : "//div[@id='sanphamCenter']/table//tr/td/table//tr[2]/td[3]",
    'category' : "",
    'description' : "//div[@id='sanphamContent']/div[3]/p/img/@src | //div[@id='sanphamContent']/div[3]",
    'images' : "//div[@id='sanphamCenter']/table//tr/td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bilyshop.net'
allowed_domains = ['bilyshop.net']
start_urls = ['http://bilyshop.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/sanphamcosan_+[a-zA-Z0-9-]+_+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danhmuccosan_+[a-zA-Z0-9-]+_+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
