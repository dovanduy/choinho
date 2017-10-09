# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='p_name']",
    'price' : "//div[@class='div_price_detail']/table//tr[2]/td[2]/span[@class='price']",
    'category' : "//div[@class='navation']/text()|//div[@class='navation']/a",
    'description' : "//div[@class='bg_tab']/div[@class='subinfoInner']",
    'images' : "//ul[@class='sliders-wrap-inner']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'muatoday.com.vn'
allowed_domains = ['muatoday.com.vn']
start_urls = ['http://www.muatoday.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$'],deny=['collagen-cao-cap.html($|/\?p=\d+&sort=0$)','sua-ong-chua-giup-dep-da-amp-khoe-manh.html($|/\?p=\d+&sort=0$)','tri-nam-tan-nhang-amp-doi-moi.html($|/\?p=\d+&sort=0$)','cham-soc-da-mat.html($|/\?p=\d+&sort=0$)','sua-rua-mat-amp-sua-tam.html($|/\?p=\d+&sort=0$)','tri-mun-amp-seo-tham.html($|/\?p=\d+&sort=0$)','giam-can-amp-tan-mo.html($|/\?p=\d+&sort=0$)','sua-rua-mat-tay-trang-nuoc-hoa-hong.html($|/\?p=\d+&sort=0$)','chong-nhan-va-tham-quang-vung-mat.html($|/\?p=\d+&sort=0$)','mat-na-collagen-duong-da.html($|/\?p=\d+&sort=0$)','sua-duong-the-giup-min-amp-trang-da.html($|/\?p=\d+&sort=0$)','nhau-thai-cuu-duong-da-tri-nam-hieu-qua.html($|/\?p=\d+&sort=0$)','omega-3-giup-sang-mat.html($|/\?p=\d+&sort=0$)','combo-gia-re-va-khuyen-mai.html($|/\?p=\d+&sort=0$)']), 'parse_item'),
    Rule(LinkExtractor(allow=['collagen-cao-cap.html($|/\?p=\d+&sort=0$)','sua-ong-chua-giup-dep-da-amp-khoe-manh.html($|/\?p=\d+&sort=0$)','tri-nam-tan-nhang-amp-doi-moi.html($|/\?p=\d+&sort=0$)','cham-soc-da-mat.html($|/\?p=\d+&sort=0$)','sua-rua-mat-amp-sua-tam.html($|/\?p=\d+&sort=0$)','tri-mun-amp-seo-tham.html($|/\?p=\d+&sort=0$)','giam-can-amp-tan-mo.html($|/\?p=\d+&sort=0$)','sua-rua-mat-tay-trang-nuoc-hoa-hong.html($|/\?p=\d+&sort=0$)','chong-nhan-va-tham-quang-vung-mat.html($|/\?p=\d+&sort=0$)','mat-na-collagen-duong-da.html($|/\?p=\d+&sort=0$)','sua-duong-the-giup-min-amp-trang-da.html($|/\?p=\d+&sort=0$)','nhau-thai-cuu-duong-da-tri-nam-hieu-qua.html($|/\?p=\d+&sort=0$)','omega-3-giup-sang-mat.html($|/\?p=\d+&sort=0$)','combo-gia-re-va-khuyen-mai.html($|/\?p=\d+&sort=0$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
