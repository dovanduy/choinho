# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_name']",
    'price' : "//div[@class='addToCartSection']//span[@class='current-price']",
    'category' : "//div[@id='contentBody']/div[@id='catMaps']/a",
    'description' : "//div[@class='bodyContent']/div[@class='page-section' and not (@id='productCommentsSection')]",
    'images' : "//ul[@id='etalage']/li/div/img/@src | //td[@id='detailImageContainer']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'echo.com.vn'
allowed_domains = ['echo.com.vn']
start_urls = ['http://echo.com.vn/welcome']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/pds/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/selectcat/','/pbr/'], deny=['makerName=','origin=','ratingScore=','\d+_s=','\d+_td=','\d+_[a-zA-Z]+=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]