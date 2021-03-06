# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='wrapper']/div[@id='content']/div[@class='pro_detail_name']/h1",
    'price' : "//div[@class='image']/center/div[@class='pd_price_value']/span[@class='red b']",
    'category' : "//div[@id='content']/div[@id='pro_detail_name']/div[@id='nav_link']/a",
    'description' : "//div[@id='pro_detail']/div[@id='pro_tabs']/div[@class='panes']/div[@id='pro_detail_label']",
    'images' : "//div[@class='image']/div/a[@class='zoom_in']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhathuoc365.vn'
allowed_domains = ['nhathuoc365.vn']
start_urls = ['http://nhathuoc365.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
