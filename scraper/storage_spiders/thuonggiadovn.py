# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box_product_detail_right']/div[1]/h1 | //div[@class='slider-products-title']/h1/span",
    'price' : "//div[@class='simple-prop']/p[4]/span",
    'category' : "//ol[@class='breadcrumb']/li/a",
    'description' : "//div[@class='tab-content']/div[@id='home']",
    'images' : "//div[@id='product_detail_img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thuonggiado.vn'
allowed_domains = ['thuonggiado.vn']
start_urls = ['http://www.thuonggiado.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/tagcat+\d+/', '/tag+\d+/','Danh-muc']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]