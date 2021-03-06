# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='tamnhin_detail_page']/div[@class='product_detail_info']/div[@class='detail_pro']/h1",
    'price' : "//div[@class='product_detail_info']/div[@class='price_detail']/span/b",
    'category' : "//div[@class='column_center right']/div[@id='tamnhin_detail_page']/div[@id='cat_path']/a",
    'description' : "//div[@class='column_center right']/div[@id='tamnhin_detail_page']/div[@class='boxDetailBorder']/div[@id='content_2']",
    'images' : "//div[@id='productImageBox']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tamnhin.com.vn'
allowed_domains = ['tamnhin.com.vn']
start_urls = ['http://www.tamnhin.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
