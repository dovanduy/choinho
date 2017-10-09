# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h2[@class='tt-md upper text-orange']",
    'price' : "//div[@class='inline']/span[@class='price']",
    'category' : "//ol[@class='breadcrumb']/li/a",
    'description' : "//section[@class='block-tabs-out']/div[@class='tab-content']",
    'images' : "//div[@class='slide-lg-item']/a[@class='block']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'bevadochoi.com'
allowed_domains = ['bevadochoi.com']
start_urls = ['http://bevadochoi.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet-[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/$'], deny=['/chi-tiet-[a-zA-Z0-9-]+/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]