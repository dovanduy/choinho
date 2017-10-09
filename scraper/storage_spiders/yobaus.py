# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='div_col_right']/h1[@class='h1_title_main_product']",
    'price' : "//p[@class='p_text_main_product']/span[@class='s_price_main_product']",
    'category' : "//ul[@class='ul_path']/li/a",
    'description' : "//div[@class='tab_container']/div[@id='tab0']",
    'images' : "//div[@id='carousel']/a/img/@src | //div[@id='thumbs']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'yoba.us'
allowed_domains = ['yoba.us']
start_urls = ['http://yoba.us/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+s+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]