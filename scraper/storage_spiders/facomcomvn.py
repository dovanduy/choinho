# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='border_box_detail']/div[@class='product_detail_info']/div[@class='detail_pro']/h1",
    'price' : "//div[@class='product_detail_info']/div[@class='product_detail_info_r left']/div[@class='price_detail_']/span",
    'category' : "//div[@class='border_box_detail_c left']/div/div[@id='cat_path']/a",
    'description' : "//div[@id='main']/div[@class='column_right left']/div[@class='border_box_detail']/div[@class='boxDetailBorder']",
    'images' : "//div[@id='gallery']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'facom.com.vn'
allowed_domains = ['facom.com.vn']
start_urls = ['http://facom.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_dm+\d+\.html'], deny=['&']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
