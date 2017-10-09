# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@itemprop='offers']/span[@class='price']/span[@itemprop='price']",
    'category' : "//div[@class='breadcrumb']/div[@class='container']/ol/a",
    'description' : "//div[@class='tab-pane active first']/div[@class='block__content clearfix']",
    'images' : "//a/img[@itemprop='image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "//div[@class='product__details']/div[@class='product__description']/ul/li[2]",
    'in_stock' : "//div[@class='product__details']/div[@class='product__description']/ul/li[3]/span",
    'guarantee' : "",
    'promotion' : ""
}
name = 'hangre247.vn'
allowed_domains = ['hangre247.vn']
start_urls = ['https://hangre247.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]