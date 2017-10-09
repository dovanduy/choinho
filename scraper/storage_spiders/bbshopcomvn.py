# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//form[@id='buy_product']/div[@class='price-num']/div[@class='price']/span[@class='price-new']",
    'category' : "//section[@class='breadcrumbs clearfix']/a",
    'description' : "//section[@id='product-tab']/ul[@class='tab']/p",
    'images' : "//img[@id='main_img']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bbshop.com.vn'
allowed_domains = ['bbshop.com.vn']
start_urls = ['http://bbshop.com.vn/danh-sach-san-pham.html']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-sach-san-pham(/\d+)*\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
