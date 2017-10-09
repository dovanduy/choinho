# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td[@id='name']/h1",
    'price' : "//tr/td[@id='td_info']/font",
    'category' : "//div[@class='w1120']/div[@class='w1120']/div[@id='homeaddress']/a",
    'description' : "//div[@id='detail']/div[@id='detail-product']/div[@id='dp-description']/div[@id='dpd-main']",
    'images' : "//tr/td/a[@id='id_sanpham']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hoangphatvn.vn'
allowed_domains = ['hoangphatvn.vn']
start_urls = ['http://hoangphatvn.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html','/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
