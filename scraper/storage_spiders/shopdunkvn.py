# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productName']/h1",
    'price' : "//div[@class='product_right sp-bd-r']/span/b[@class='giacuahang price'] | //div[@class='it_row']/div[@class='product_right sp-bd-r']/span/b[@class='giacuahang price']",
    'category' : "",
    'description' : "//div[@class='it_row']/div[@class='pr_detail_tbs sp-bd-l']/div[@class='it_row_center_detail']/div[@class='it_row_center_te inf']",
    'images' : "//div[@class='imgs']/div[@class='img-a']/img/@src | //div[@class='oneByOne1']/div[@id='banner']/div[@class='oneByOne_item']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'shopdunk.vn'
allowed_domains = ['shopdunk.vn']
start_urls = ['http://shopdunk.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
