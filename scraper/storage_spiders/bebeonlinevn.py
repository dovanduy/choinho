# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='block-pack']/ul/li/h1",
    'price' : "//table[@class='product_details']//tr/td/span",
    'category' : "//div[@class='block-pack']/ul/li/a",
    'description' : "//div[@class='block-ct']/div[@class='text-info']",
    'images' : "//div[@class='product_thumbnail']/a/div[@class='zoomPad']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bebeonline.vn'
allowed_domains = ['bebeonline.vn']
start_urls = ['http://bebeonline.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/+[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
