# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product-detail-name']",
    'price' : "//span[@class='price']",
    'category' : "//div[@class='crumb']/a",
    'description' : "//div[@class='tab-product-detail']",
    'images' : "//div[@class='pro-image col-1-2 w700px-1 w700px-padding-right0']//a[1]/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthigagoi.com'
allowed_domains = ['sieuthigagoi.com']
start_urls = ['http://www.sieuthigagoi.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/($|page-\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]