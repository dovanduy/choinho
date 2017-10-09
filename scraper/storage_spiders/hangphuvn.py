# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title_code_pro']/font/h1/span",
    'price' : "//div[@class='product_detail_right']/div[@class='content_ct']/p[@class='price_km']/span",
    'category' : "//div[@class='navigater_pro']/div/a/span",
    'description' : "//div[@class='content_right']/div[@class='products_home']/div[@class='thong_tin_san_pham']/div[@class='tabs_content_container']",
    'images' : "//div[@class='slide_product']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hangphu.vn'
allowed_domains = ['hangphu.vn']
start_urls = ['http://hangphu.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet-san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
