# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/div[@class='container']/div[@class='wrapper']/div[@class='right_content']/div[@class='mid_content']/div[@class='ct-div-sub product-detail']/div[@class='product-infos']/h1",
    'price' : "/html/body/div[@class='container']/div[@class='wrapper']/div[@class='right_content']/div[@class='mid_content']/div[@class='ct-div-sub product-detail']/div[@class='product-infos']/ul[@class='list_info_pro_dt']/li[5]",
    'category' : "/html/body/div[@class='container']/div[@class='wrapper']/div[@class='right_content']/div[@class='mid_content']/div[@class='title-h3 topNavigation']/ul[@class='navigation']/li/a/span",
    'description' : "/html/body/div[@class='container']/div[@class='wrapper']/div[@class='right_content']/div[@class='mid_content']/div[@class='ct-div-sub product-detail']/div[@class='description']/p",
    'images' : "/html/body/div[@class='container']/div[@class='wrapper']/div[@class='right_content']/div[@class='mid_content']/div[@class='ct-div-sub product-detail']/div[@class='img_info_pro']/a[@id='fancy_pro_img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tiensilanda.vn'
allowed_domains = ['tiensilanda.vn']
start_urls = ['http://www.tiensilanda.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
