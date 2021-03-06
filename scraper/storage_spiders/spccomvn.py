# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='top_prodetail']/div[@id='overview']/h1",
    'price' : "//div[@id='overview']/p[@id='price_detail']/span[2]",
    'category' : "//ul[@class='cate-nav']/li/a",
    'description' : "//div[@id='tab1']/table[@id='tb-product-spec']",
    'images' : "//div[@id='img_detail']/div[@id='img_large']/a/@href | //div[@id='img_thumb']/div[@class='caroufredsel_wrapper']/ul[@class='ul']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'spc.com.vn'
allowed_domains = ['spc.com.vn']
start_urls = ['http://spc.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html'], deny=['filter=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
