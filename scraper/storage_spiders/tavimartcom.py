# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='proDetail_img']/div[@class='tabsphot']/span",
    'price' : "//div[@class='item_price_cus']/div/span[@class='priceDetail']",
    'category' : "//div[@id='products']/div[@class='sphot_name']/a",
    'description' : "//div[@class='CaptabDescInfor_ tabContent']/div[1]",
    'images' : "//div[@class='prodetail_left']//a/@data-zoom-image | //div[@class='prodetail_left']//div/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'tavimart.com'
allowed_domains = ['tavimart.com']
start_urls = ['http://tavimart.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/cat+\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
