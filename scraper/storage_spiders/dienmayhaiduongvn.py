# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@class='box_prices clearfix']/span[@itemprop='price']",
    'category' : "",
    'description' : "//div[@class='panel-collapse collapse in']/div[@class='panel-body']/div[@class='rte']",
    'images' : "//meta[@property='og:image'][1]/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "//h5[@itemprop='brand']/a",
    'in_stock' : "//div[@class='availability']/p[@class='available instock']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dienmayhaiduong.vn'
allowed_domains = ['dienmayhaiduong.vn']
start_urls = ['http://dienmayhaiduong.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]