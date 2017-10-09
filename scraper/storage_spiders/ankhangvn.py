# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='overview']/h1",
    'price' : "//div[@id='price_detail']/div[@class='img_price_full']",
    'category' : "//div[@id='breadcrumb']/div/a/span",
    'description' : "//div[@id='overview']/div[@class='content_scroll_tab']/p",
    'images' : "//div[@id='img_detail']/ul[@class='ul']/li/a/@href|//div[@id='img_detail']/div[@id='img_large']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'ankhang.vn'
allowed_domains = ['ankhang.vn']
start_urls = ['http://www.ankhang.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+_id\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+_dm\d+\.html($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
