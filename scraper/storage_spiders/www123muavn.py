# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info-inner']/h1[@id='title-product'] | //div[@class='box-des-rg']/span[@class='name-product']",
    'price' : "//div[@class='price']/span[@id='sub_price']",
    'category' : "//div[@class='link-site-more']/a/strong/span",
    'description' : "//div[@class='detail-desc']/div[@id='tab1'] | //div[@class='detail-desc']/div[@id='tab2']/p",
    'images' : "//ul[@id='img-gallerySlider']//span/@id",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = '123mua.vn'
allowed_domains = ['123mua.vn']
start_urls = ['http://www.123mua.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/u+\d+/[a-zA-Z0-9-]+($|\?page=\d+)'], deny=['/dich-vu-ban-the.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
