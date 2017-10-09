# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='overview']/h1",
    'price' : "//div[@class='img_price_full_large']",
    'category' : "//div[@id='location']/a",
    'description' : "//div[@class='container']/div[@id='pro_detail_page']/div[@id='product_detail']/div[@id='tab1']",
    'images' : "//div[@id='img_detail']/div[@id='img_large']//img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'anphatpc.com.vn'
allowed_domains = ['anphatpc.com.vn']
start_urls = ['http://www.anphatpc.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_dm+\d+\.html($|\?page=\d+$)'], deny =['/page/','tintuc','\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
