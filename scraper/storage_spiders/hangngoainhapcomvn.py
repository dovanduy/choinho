# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//span[@class='pro-price']/span",
    'category' : "//div[@id='ur_here']/a",
    'description' : "//div[@class='inDetail_box']/div[@id='no_try_record']",
    'images' : "//li[@class='cur']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'hangngoainhap.com.vn'
allowed_domains = ['hangngoainhap.com.vn']
start_urls = ['http://hangngoainhap.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/\d+-[\w-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-\d+-b0-([\w-]+|min0-max0-attr0-\d+-shop_price-ASC-)\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
