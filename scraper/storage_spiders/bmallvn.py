# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='group-product-info']/h1",
    'price' : "//div[@class='group-product-info']/div[@class='product-info sell-price']/span[@class='uc-price']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='field-items']/div[@class='field-item even']/h3",
    'images' : "//ul/li/a[@class='fancybox']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//div[@class='product-extra-info']/div[@class='field field-name-field-trang-thai field-type-list-integer field-label-inline clearfix']/div[@class='field-items']/div[@class='field-item even']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'bmall.vn'
allowed_domains = ['bmall.vn']
start_urls = ['http://bmall.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['\.html']), 'parse_item_and_links'),
]
