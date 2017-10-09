# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='name']",
    'price' : "//div[@class='price-sales']/span[@class='price']",
    'category' : "//div[@class='bg-title-main']/div/a/span",
    'description' : "//div[@class='shop-content']/div[@class='content']/div[1]",
    'images' : "//div[@class='sp_d_img']/div/div/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'alobuy.vn'
allowed_domains = ['alobuy.vn']
start_urls = ['http://alobuy.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/chuyen-muc/[a-zA-Z0-9-]+-\d+(\.html$|/0/0/\d+/$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
