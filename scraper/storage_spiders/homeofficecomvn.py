# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='ty-product-block__left']/form/h1[@class='ty-product-block-title']",
    'price' : "//div[@class='ty-product-block__price-actual']/span",
    'category' : "//div[@class='ty-breadcrumbs clearfix']/a",
    'description' : "//div[@id='content_description']/div/p",
    'images' : "//div[@class='ty-product-block__img-wrapper']//a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'homeoffice.com.vn'
allowed_domains = ['homeoffice.com.vn']
start_urls = ['http://homeoffice.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
