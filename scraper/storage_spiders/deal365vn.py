# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail-intro']/table[@class='thong_tin']//tr[1]/td/h3/a[@class='thongtin_s']/span",
    'price' : "//div[@class='detail-intro']/table[@class='thong_tin']//tr[2]/td[@class='thongtin_s real_price'] | //div[@class='detail-intro']/table[@class='thong_tin']//tr[3]/td[@class='thongtin_s'][2]",
    'category' : "//div[@class='dk_product_content']/ul[@id='breadcrumbs-one']/li/span/a",
    'description' : "//div[@class='dk_product_content green_gradient_background']/div/ul | //div[@class='dk_product_content green_gradient_background']/div/ul/li/img/@src",
    'images' : "//div[@class='minh_hoa']/a[1]/img[@class='product_image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'deal365.vn'
allowed_domains = ['deal365.vn']
start_urls = ['http://deal365.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
