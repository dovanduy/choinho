# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='chi-tiet']/div[@id='right-chitiet']/h1[@id='title-sp']",
    'price' : "//div[@class='price_in_tab full']/p[@class='left']",
    'category' : "//div[@class='breadcrumb']/div[@id='breadcrumbs']/a",
    'description' : "//div[@class='tab_content']/div[@class='the_content']",
    'images' : "//div[@id='anh-con']/div/img/@src | //div[@class='swiper-slide']/img[@class='thumb_img']/@src | //meta[@property='og:image']/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'dienthoaidoc.com'
allowed_domains = ['dienthoaidoc.com']
start_urls = ['http://dienthoaidoc.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/'],deny=['tin-tuc']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]