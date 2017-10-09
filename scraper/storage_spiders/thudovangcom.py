# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='boxsp-chitiet']/div[@class='boxsp-chitiet-masp'][1]",
    'price' : "//div[@class='boxsp-chitiet-gia']/span[@class='gia1']",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='boxsp-chitiet-img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thudovang.com'
allowed_domains = ['thudovang.com']
start_urls = ['http://thudovang.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+\.aspx$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c-\d+\.aspx$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
