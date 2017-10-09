# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='rightContent']/div[@class='intro']/h1",
    'price' : "//span[@class='price']",
    'category' : "//div[@class='navigation']/ul/li/a",
    'description' : "//div[@class='rightContent']/div[@class='intro']/ul/li",
    'images' : "//div[@id='verGallery']/div[@class='photoInfo']/p/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'eshop24h.vn'
allowed_domains = ['eshop24h.vn']
start_urls = ['http://eshop24h.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/gia-re+/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]