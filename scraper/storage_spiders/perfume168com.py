# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='primary_block']/div/h1",
    'price' : "//td[@class='p-sale'] | //td[@class='price'][1]",
    'category' : "//div[@class='breadcrumb_inner']/span/a",
    'description' : "//div[@class='cont']/div[@class='des']",
    'images' : "//div[@id='thumbs_list']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'perfume168.com'
allowed_domains = ['perfume168.com']
start_urls = ['http://perfume168.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+\.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-p.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
