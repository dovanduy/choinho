# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title']/h2",
    'price' : "//p[@class='pridis']/strong",
    'category' : "",
    'description' : "//div[@class='detail']",
    'images' : "//div [@class='sllist']/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'necdeal.vn'
allowed_domains = ['necdeal.vn']
start_urls = ['http://necdeal.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/deal/[a-z0-9-]+/[a-z0-9-]+-[a-z0-9]+'], deny = ['.*/$']), 'parse_item'),
    Rule(LinkExtractor(deny = ['.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
