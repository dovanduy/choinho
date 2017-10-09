# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content_detail']/div[@class='extra_title width880']",
    'price' : "//div[@id='product_price']/div[@id='ctl00_ContentPlaceHolder1_dtpro_ctl00_product_price_right2']",
    'category' : "",
    'description' : "//div[@id='info_right']/div[@id='product_detail']",
    'images' : "//div[@id='product_image']/div[@id='product_pic']/div[@id='wrap']/a/img/@src | //a[@class='cloud-zoom-gallery']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'babyclick.vn'
allowed_domains = ['babyclick.vn']
start_urls = ['http://babyclick.vn/Trang-chu/Cho-be.aspx']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['\*.aspx']), 'parse_item'),
    Rule(LinkExtractor(deny=['/Khuyen-mai.aspx', '/Tin-tuc.aspx', '/Lien-he.aspx','/Gio-hang.aspx','/Gioi-thieu.aspx','/Cach-mua-hang.aspx','/Cach-thanh-toan.aspx']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
