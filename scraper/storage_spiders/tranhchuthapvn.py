# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='clearfix']/div[@class='product-info']/form[@class='cm-disable-empty-files cm-required-form cm-ajax cm-ajax-full-render']/h1[@class='mainbox-title']",
    'price' : "//p[@class='actual-price']/span/span",
    'category' : "//div[@class='grid_16 ']/div[@id='breadcrumbs_26']/div[@class='breadcrumbs clearfix']/a",
    'description' : "//div[@class='grid_12 ']/div[@class=' noidung']/div[@class='product-main-info']/div[@id='tabs_content']",
    'images' : "//div/div[@class='cm-image-wrap']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tranhchuthap.vn'
allowed_domains = ['tranhchuthap.vn']
start_urls = ['http://tranhchuthap.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
