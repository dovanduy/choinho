# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prd-details l-cell']/h3",
    'price' : "//span[@class='prd-price strong']/span[@id='special_price_box']",
    'category' : "//div[@id='crumlist']/a",
    'description' : "//div[@id='example-two2']/div[@class='list-wrap']",
    'images' : "//div[@class='zoom-section']/div[@class='zoom-small-image']/div/a/@href | //div[@class='zoom-desc']/p/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dnmart.vn'
allowed_domains = ['dnmart.vn']
start_urls = ['http://dnmart.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet-san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/'], deny=['kg=','th=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
