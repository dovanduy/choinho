# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-page-details-sp']/h3",
    'price' : "//div[@class='product-page-details-sp']/span[1]/p[@class='gia']",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='border span12 shadow product-page-details']/div[@class='tab-content']",
    'images' : "//div[@id='gallery']/div[@id='slides']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dem.vn'
allowed_domains = ['dem.vn']
start_urls = ['http://dem.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$'], deny=['/gioi-thieu-dem-vn', '/chinh-sach-chat-luong', '/huong-dan-mua-hang', '/dieu-khoan-su-dung', '/chinh-sach-bao-mat', '/component/', '/Lien-he', 'Mua-chung', '/$', 'com_content','index.php', 'virtuemart', 'nganluong', 'smartseo.vn', 'livehelp', '.vn/&']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
