# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td[@class='cssdtTitle']/span[@id='dnn_ctr523_Main_ProductDetail_SP_TEN']",
    'price' : "//tr/td/span[@class='cssdetailgia']/span",
    'category' : "",
    'description' : "//div[@id='dnn_ctr523_ModuleContent']/div[@id='dnn_ctr523_Main_ProductDetail_up']/div[@class='divInfo']/table[@class='productInfo']",
    'images' : "//div[@class='cssImgBase monitor']/div[@id='wrap']/a[@id='zoom1']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'anhhongmobile.com.vn'
allowed_domains = ['anhhongmobile.com.vn']
start_urls = ['http://anhhongmobile.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chitietsp.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow=['/productsearch.aspx']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]