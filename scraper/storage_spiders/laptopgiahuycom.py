# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='head-center']/h2[@id='productname']",
    'price' : "//div[@class='dienmay']/div[@class='pricedienmay']/span[@class='pricenew']",
    'category' : "//div[@class='navbarprod asdasd']/ul/li/a",
    'description' : "//div[@id='articles']/ul",
    'images' : "//div[@id='zoomslide']/div[@class='fixzoom']/img[@id='zoom']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'laptopgiahuy.com'
allowed_domains = ['laptopgiahuy.com']
start_urls = ['http://www.laptopgiahuy.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/', '/\d+-[a-zA-Z0-9-]+\.html]']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
