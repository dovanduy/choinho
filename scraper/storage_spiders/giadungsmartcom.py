# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tensp']/h2",
    'price' : "//div[@class='pd-right fr']/p[@class='p-price']",
    'category' : "//ul[@class='breadcrumb all']/li/a",
    'description' : "//div[@class='p-introduct all']/div[@class='content_tab_all']",
    'images' : "//ul[@class='list_small']/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'giadungsmart.com'
allowed_domains = ['giadungsmart.com']
start_urls = ['http://giadungsmart.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d.*\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html($|\?Page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
