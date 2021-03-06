# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='span11 ']/div[@class='product-main-info']/div[@class='clearfix']/h1[@class='mainbox-title']",
    'price' : "//p[@class='actual-price']/span/span/span",
    'category' : "//div[@class='span11']/div[@id='breadcrumbs_26']/div[@class='breadcrumbs clearfix']/a",
    'description' : "//div/div[@class='product-main-info']/div[@id='content_description']",
    'images' : "//div[@class='clearfix']/div[@class='image-wrap']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthilamdep.com'
allowed_domains = ['sieuthilamdep.com']
start_urls = ['http://sieuthilamdep.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
