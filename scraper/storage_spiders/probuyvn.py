# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tittle_7']/h1[@class='h1_title_7']/span",
    'price' : "//div/div[@class='gia_sp_khuyenmai']/span",
    'category' : "",
    'description' : "//div[@class='chitiet_noidung']/div[@class='pro_detaii_desc']/span",
    'images' : "//div[@class='chitiet_img']/div[2]/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'probuy.vn'
allowed_domains = ['probuy.vn']
start_urls = ['http://probuy.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/sanpham/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/gianhang/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
