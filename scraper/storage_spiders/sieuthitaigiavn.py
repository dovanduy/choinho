# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pro-detail-info']/h1",
    'price' : "//div[@class='product-price'][2]/div[@class='product-price-val']",
    'category' : "//a[@itemprop='url']/span[@itemprop='title']",
    'description' : "//div[@class='tabContainer']/div[@class='tabContent contEditor']",
    'images' : "//ul[@class='pro-thumbs-list']/li[@class='current']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "//div[@class='product-price'][3]/div[@class='product-price-val']",
    'promotion' : ""
}
name = 'sieuthitaigia.vn'
allowed_domains = ['sieuthitaigia.vn']
start_urls = ['http://www.sieuthitaigia.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[\w-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w-]+/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
