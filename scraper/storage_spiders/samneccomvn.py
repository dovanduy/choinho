# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='thong-tin-gia']/h1[@class='node-title']",
    'price' : "//span[@class='gia-vat']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='quicktabs-container-thong_tin_san_pham']",
    'images' : "//div[@class='sliderkit-panel'][1]//img[@typeof]/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'samnec.com.vn'
allowed_domains = ['samnec.com.vn']
start_urls = ['http://samnec.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?sell_price=.sell_price_1=.keys=.page=\d+)'], deny=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]