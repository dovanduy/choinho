# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_detail_info']/div[@class='detail_pro']/h1",
    'price' : "//div[@class='product_detail_info']/div[@class='price_detail']/span/b",
    'category' : "//div[@id='tamnhin_detail_page']/div[@id='cat_path']/a",
    'description' : "//div[@class='boxDetailBorder']/div[@id='content_1']",
    'images' : "//div[@class='product_detail_image']/div/div[@id='productImageBox']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'saomaidienmay.com'
allowed_domains = ['saomaidienmay.com']
start_urls = ['http://saomaidienmay.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]