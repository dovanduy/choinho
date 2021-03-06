# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//p[@class='special-price']/span[@class='price']|//span[@class='regular-price']/span[@class='price']",
    'category' : "//ul[@class='breadcrumbs']/li/a",
    'description' : "//div[@id='ja-tab-description']/div[@class='box-collateral box-description']",
    'images' : "//div[@class='more-views']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = '2teck.com'
allowed_domains = ['2teck.com']
start_urls = ['http://2teck.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[\w-]+\.html($|\?p=\d+$)']), 'parse_item_and_links'),
]
