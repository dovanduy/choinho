# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='ty-product-block-title']",
    'price' : "//div[@class='ty-product-block__price-actual']/span/span/span",
    'category' : "//div[@class='span16 breadcrumbs-grid']/div[@id='breadcrumbs_1']/div[@class='ty-breadcrumbs clearfix']/a",
    'description' : "//div[@class='row-fluid ']/div[@class='span16 main-content-grid']/div[@class='ty-product-block']/div[@id='tabs_content']",
    'images' : "//a[@class='cm-image-previewer cm-previewer ty-previewer']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'phuthai.vn'
allowed_domains = ['phuthai.vn']
start_urls = ['http://phuthai.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(allow=['']), 'parse_item'),
    #Rule(LinkExtractor(allow=['']), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/$']), 'parse_item_and_links'),
]