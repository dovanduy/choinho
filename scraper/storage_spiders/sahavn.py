# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='row'][1]/div/div[@class='sell-price']",
    'category' : "//div[@class='breadcrumbs breadcrumb']/ul/li/a/span",
    'description' : "//div[@class='product-terms-inner-in']/div[@class='row']/div[@class='span6 product-feature']",
    'images' : "//ul[@class='sliders-wrap-inner']/li/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'saha.vn'
allowed_domains = ['saha.vn']
start_urls = ['http://www.saha.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-[\w\d]+\d[\w\d]+\.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
