# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='new_items_title_top']/a",
    'price' : "//div[@class='new_items_content_info_gia png']/div[2]",
    'category' : "",
    'description' : "//div[@class='new_items_content_info_col2_content_info']",
    'images' : "//div[@class='new_items_content_info_col2']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'remoingay.com'
allowed_domains = ['remoingay.com']
start_urls = ['http://remoingay.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['.html$'], deny = ['dang-ky', 'dang-nhap', 'thong-bao', 'huong-dan', 'quy-che', 'hop-tac', 'lien-he', 'tuyen-dung', 'don-hang','hoi-dap','toxml','/website', 've-chung-toi']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
