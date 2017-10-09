# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//p[@class='price']//span[@class='amount']",
    'category' : "//nav[@itemprop='breadcrumb']/a",
    'description' : "//div[@class='woocommerce-tabs wc-tabs-wrapper']/div[@class='panel entry-content wc-tab']",
    'images' : "//div[@class='images']/a[@itemprop='image']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'shopgiaphat.com'
allowed_domains = ['shopgiaphat.com']
start_urls = ['http://shopgiaphat.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z0-9-]+/($|page/\d+/$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
