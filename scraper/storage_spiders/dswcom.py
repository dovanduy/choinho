# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1/div[@itemprop='name']",
    'price' : "//div[@itemprop='priceCurrency']/span[@itemprop='price']",
    'category' : "",
    'description' : "//div[@class='product-detail__product-description-row']/div[@class='product-detail__descr-width']",
    'images' : "//div[@class='carousel-inner']/div[@class='item text-center active']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dsw.com'
allowed_domains = ['dsw.com']
start_urls = ['https://www.dsw.com/en/us/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/product/[a-zA-Z0-9-]+/\d+']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/[a-zA-Z0-9-/]+\?No=\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]