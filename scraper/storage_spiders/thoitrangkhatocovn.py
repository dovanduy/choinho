# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='block-content']/h2[@class='condensed']",
    'price' : "//div[@class='grid9 fl pr0']/p[@class='item-price condensed']/text()",
    'category' : "//div[@class='breadcrumb fl']/a",
    'description' : "//div[@class='block-content']/div[@class='tablist clearfix']/div[@class='the-content']",
    'images' : "//ul[@class='preview-image list-style-none']/li[@class='elevate']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'thoitrangkhatoco.vn'
allowed_domains = ['thoitrangkhatoco.vn']
start_urls = ['http://thoitrangkhatoco.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/$'], deny=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/($|page/\d+/$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
