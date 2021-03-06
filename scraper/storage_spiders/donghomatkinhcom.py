# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='mglr_9']/div[@class='detailProduct']/div[@class='infoProduct']/h1[@class='tip']",
    'price' : "//div[@class='detailProduct']/div[@class='infoProduct']/div[@class='txPro ui-mark']/span[@id='_giasp']",
    'category' : "//div[@id='breadcum_wp']/ul[@id='bcrumb']/li/a",
    'description' : "",
    'images' : "//div[@class='detailProduct']/div[@class='thumnailProduct']/div[@class='thumnailProduct']/div[@class='small-img']//img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'donghomatkinh.com'
allowed_domains = ['donghomatkinh.com']
start_urls = ['http://donghomatkinh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-1+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
