# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title-product workshome-title']/h3",
    'price' : "//div[@class='PricesalesPrice']/span[@class='PricesalesPrice']",
    'category' : "",
    'description' : "//div[@class='tabDetails']/div[@class='tabContents']/div[@class='product-content-detail']//p",
    'images' : "//div[@class='main-image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'dienmaytoanlinh.vn'
allowed_domains = ['dienmaytoanlinh.vn']
start_urls = ['http://www.dienmaytoanlinh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/gian-hang-ban/.+-\d+-detail\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/gian-hang-ban/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
