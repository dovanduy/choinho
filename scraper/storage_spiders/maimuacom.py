# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h3[@class='title-produt-']|//h1[@class='title-produt-']",
    'price' : "//div[@class='price']/div[@class='price-gruop']",
    'category' : "//ol[@class='breadcrumb']/li/a",
    'description' : "//div[@class='tabs-group box']/div[@id='tab-description']",
    'images' : "//div[@class='item clearfix']/a/@href | //img[@id='image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'maimua.com'
allowed_domains = ['maimua.com']
start_urls = ['http://maimua.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(deny=['/dien-gia-dung','/dien-thoai-may-tinh-bang','/may-vi-tinh-laptop','/me-va-be','/suc-khoe-va-lam-dep','/thoi-trang','/ba-lo-tui-xach','/may-anh-may-quay-phim','/nha-cua-doi-song','/qua-tang-do-luu-niem','\??page=\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/dien-gia-dung','/dien-thoai-may-tinh-bang','/may-vi-tinh-laptop','/me-va-be','/suc-khoe-va-lam-dep','/thoi-trang','/ba-lo-tui-xach','/may-anh-may-quay-phim','/nha-cua-doi-song','/qua-tang-do-luu-niem','\??page=\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
