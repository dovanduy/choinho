# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1",
    'price' : "//div[@id='main-content']/div[@id='left-column']/div/p[1]",
    'category' : "//div[@id='breadcrumbs']/a",
    'description' : "//div[@id='main-content']/div[@id='left-column']/div/p | //div[@id='main-content']/div[@id='left-column']/div/p/a/img/@src",
    'images' : "//div[@id='product-slides']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'cubicfun.vn'
allowed_domains = ['cubicfun.vn']
start_urls = ['http://cubicfun.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
