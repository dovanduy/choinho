# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='divr']/div[@class='pdl']/h1",
    'price' : "//ul[@class='ugs']/li/b",
    'category' : "//div[@class='dlink']/a",
    'description' : "//div[@class='divr']/div[6]",
    'images' : "//div[@class='pdl']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'soloha.vn'
allowed_domains = ['soloha.vn']
start_urls = ['http://soloha.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
