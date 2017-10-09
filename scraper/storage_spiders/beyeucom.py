# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product-details-top']/div[@class='product-name']/span",
    'price' : "//div[@id='product-details-top']/div[@class='product-detail-bg']/div[@class='price-box']/p[@class='regular-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/span/a/span",
    'description' : "//div[@class='content']/p",
    'images' : "//div[@class='onsale_big']/p//a/@href",
    'canonical' : "//link[rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'beyeu.com'
allowed_domains = ['beyeu.com']
start_urls = ['http://beyeu.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]