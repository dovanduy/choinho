# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table[@class='product_detail']//tr[1]/td/strong",
    'price' : "//table[@class='product_detail']//tr[8]/td/strong",
    'category' : "//div[@class='center_panel']/div[@class='box_center']/div[@class='box_center_title']/span",
    'description' : "//div[@class='box_center_content']/table//tr[3]/td/div",
    'images' : "//div[@class='bg_limg']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sachbanquyen.vn'
allowed_domains = ['sachbanquyen.vn']
start_urls = ['http://sachbanquyen.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]