# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='L_box_detail_ptoduct']/div[@class='tittle_detail_ptoduct']",
    'price' : "//div[@class='info_detail_ptoduct']/div/font[2]/span[@id='ctl00_ContentPlaceHolder1_ProductDetail1_detail_ctl00_lblprice']",
    'category' : "//div[@class='L_tittle_product_home L_tittle_product_home2']/a",
    'description' : "//div[@class='box_info_detail']/div[2]",
    'images' : "//div[@class='pic_detail_ptoduct']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'osc.vn'
allowed_domains = ['osc.vn']
start_urls = ['http://osc.vn/trang-chu.htm']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/pid+\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/tp+\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
