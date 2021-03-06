# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/div[@class='product-description']/h1[@class='product-name clearfix']",
    'price' : "//div[@class='price clearfix']/div[@class='price-saleoff']/span",
    'category' : "//div[@class='breadcrumb']/div[@class='ir_break']/a",
    'description' : "//div[@class='product-description']/div[@class='summary']/div[@id='rmdes']",
    'images' : "//ul[@class='ul_list_thumbnail']/li/a/@data-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'nemo.vn'
allowed_domains = ['nemo.vn']
start_urls = ['http://nemo.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-g+\d']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
