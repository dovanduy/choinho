# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-details']/h2",
    'price' : "//div/ul[@class='product-attr']/li[2] | //div/ul[@class='product-attr']/li[3]",
    'category' : "//div/span[@class='breadcrumbs pathway']/a",
    'description' : "//div/ul[@class='product-attr']/li[4]",
    'images' : "//div[@class='product-details']/table[1]//tr/td[1]/div/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'balotui.com'
allowed_domains = ['balotui.com']
start_urls = ['http://balotui.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
