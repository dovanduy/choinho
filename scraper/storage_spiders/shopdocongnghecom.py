# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='summary entry-summary single-product-info']/h1[@itemprop='name']",
    'price' : "//div[@itemprop='offers']/div/span[@class='special-price']/span[@class='woocommerce-Price-amount amount']",
    'category' : "//ul[@class='breadcrumbs']/li[@class='item']/a",
    'description' : "//div[@class='woocommerce-tabs']/div[@class='panel entry-content']",
    'images' : "//ul[@class='yith_magnifier_gallery thumbnails_carousel_list']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'shopdocongnghe.com'
allowed_domains = ['shopdocongnghe.com']
start_urls = ['http://shopdocongnghe.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z0-9-/]+/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
