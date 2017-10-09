# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product_info_top']/div[@class='box_right']/h1/font",
    'price' : "//div[@class='box_info_top']/p[@class='proPrice']/font",
    'category' : "//div[@id='product']/div[@id='breadcrumb']/a",
    'description' : "//div[@class='box_summary']/ul[@class='info_summary']/li",
    'images' : "//div[@class='thumnail_image']/ul/li/a/@href | //div[@id='product_info_top']/div[@id='box_image']/div[@class='image_large']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'knc.vn'
allowed_domains = ['knc.vn']
start_urls = ['http://knc.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]