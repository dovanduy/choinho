# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span[@id='ctl00_ctMain_ucChiTietSanPham1_lblTenSanPham']",
    'price' : "//span[@id='ctl00_ctMain_ucChiTietSanPham1_lblGia']",
    'category' : "",
    'description' : "//div[@class='cv_sp_noidung_middle']",
    'images' : "//div[@class='camera_wrap camera_amber_skin']//@data-thumb",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'cucvip.vn'
allowed_domains = ['cucvip.vn']
start_urls = ['http://cucvip.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/SanphamCT.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/Sanpham.aspx']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
