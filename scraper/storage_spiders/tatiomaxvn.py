# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='top-detail-info']/div[@class='title-detail']/h1",
    'price' : "//td/b[@style='color: red']",
    'category' : "//div[@class='title-product']/span/a",
    'description' : "//div[@class='content_tab_pro']/div[@id='chi-tiet-san-pham']/p/span/span/span",
    'images' : "//div[@class='top-detail-image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tatiomax.vn'
allowed_domains = ['tatiomax.vn']
start_urls = ['http://tatiomax.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]