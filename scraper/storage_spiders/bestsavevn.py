# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pd-right']/div[@class='pd-title']/div[@class='row']/h1",
    'price' : "//span[@class='price']/span[@class='big-red']",
    'category' : "//div[@class='menu-tree']/a",
    'description' : "//div[@class='content_Left_container']/div[@class='swap_tabcontent']/div[@id='detail_product_info']",
    'images' : "//div[@class='pd-left']/div[@class='image-view']/div//a/@href | //div[@class='product-detail']/div[@class='pd-left']/div[@class='image-view']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bestsave.vn'
allowed_domains = ['bestsave.vn']
start_urls = ['http://bestsave.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+\.htm','/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-','/\d+$','/khuyen-mai/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
