# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-right']/div[@class='pi-header-box']/div[@class='pi-box-left']/h2[@class='pi-name']",
    'price' : "//div[@class='pi-header-box']/div[@class='pi-box-right']/span[@class='pi-price']/i",
    'category' : "//div[@class='tuanda_container']/div[@id='body_content']/div[@id='nav_path']/a",
    'description' : "//div[@class='description_info']/div/span[@id='c2']",
    'images' : "//img[@id='original-zoom']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'dungvan.vn'
allowed_domains = ['dungvan.vn']
start_urls = ['http://dungvan.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+_id\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+_dm\d+\.html'], deny=['filter=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
