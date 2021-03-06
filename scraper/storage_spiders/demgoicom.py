# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product-detail']/h2[@class='heading'] | //div[@id='content']/h1[@class='entry-title']",
    'price' : "//div[@class='thongso']/ul/li[2]/span[@class='right']",
    'category' : "",
    'description' : "//div[@id='content']/div[@id='meta-data']/p | //div[@class='entry-content']/p",
    'images' : "//div[@class='Information']/div[@class='anhspsp']/img/@src | //div[@class='entry-content']/p/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'demgoi.com'
allowed_domains = ['demgoi.com']
start_urls = ['http://demgoi.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
