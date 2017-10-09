# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//p[@class='price']/span[@class='woocommerce-Price-amount amount']",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='images']/a[@itemprop='image']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'ilahui.vn'
allowed_domains = ['ilahui.vn']
start_urls = ['http://ilahui.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/$'], deny=['/san-pham/($|page/\d+/$)']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/($|page/\d+/$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
