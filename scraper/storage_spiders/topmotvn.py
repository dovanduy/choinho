# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//ol[@class='breadcrumb hidden-xs']/li[@class='active']/span",
    'price' : "//div[@class='product_brand product_padding']/div[@class='row']/div/p[@class='product_price']",
    'category' : "//ol[@class='breadcrumb hidden-xs']/li/a",
    'description' : "//div[@class='product_detail']/div[@class='row'][2]/div[@class='col-md-12 col-xs-12']",
    'images' : "//div[@id='image_sliders']/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'topmot.vn'
allowed_domains = ['topmot.vn']
start_urls = ['https://www.topmot.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/[\w-]+-\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[\w-]+($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
