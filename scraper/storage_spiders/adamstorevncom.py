# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//ul[@class='tsd']/li[1]/h1",
    'price' : "//ul[@class='tsd']/li[@class='g s5']",
    'category' : "//a[@itemprop='url']/span[@itemprop='title']",
    'description' : "//div[3]/div[@class='intro']",
    'images' : "//div[@class='small-img']/img[@id='img_01']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'adamstorevn.com'
allowed_domains = ['adamstorevn.com']
start_urls = ['http://adamstorevn.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+(/page-\d+)*\.html$']), 'parse_item_and_links'),
]
