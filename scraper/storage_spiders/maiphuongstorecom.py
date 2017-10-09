# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info-btn-ctsp']/div[@class='booksp-btnsp']/p[@class='name-ctsp']/a",
    'price' : "//div[@class='price-ctsp']/p[@class='price-root-sp']/span/span[@id='ctl00_contentMain_SanPhamChiTiet1_rptItem_ctl00_lblGia']",
    'category' : "",
    'description' : "//div[@id='ctl00_contentMain_SanPhamChiTiet1_upChiTiet']/div[@id='details-ccmt-spbc']/div[@class='info-details-sp']/div[@class='content-info-sp']",
    'images' : "//div[@class='images-products']/a[@class='imageMain']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'maiphuongstore.com'
allowed_domains = ['maiphuongstore.com']
start_urls = ['http://maiphuongstore.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['_sp+\d+_']), 'parse_item'),
    Rule(LinkExtractor(allow=['_dmsp+\d+_']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
