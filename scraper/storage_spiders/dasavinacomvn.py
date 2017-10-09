# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='product-single-price']/p[@class='price']",
    'category' : "//nav[@class='woocommerce-breadcrumb']/a",
    'description' : "//div[@class='tab-pane active']",
    'images' : "//ul[@class='yith_magnifier_gallery']/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dasavina.com.vn'
allowed_domains = ['dasavina.com.vn']
start_urls = ['http://dasavina.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z-0-9]+/($|page/\d+/)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
