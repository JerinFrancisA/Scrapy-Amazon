# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class ZonSpider(scrapy.Spider):
    name = 'zon'
    start_urls = [
        'https://www.bookmybai.com/hire-full-time-maid-and-elderly-care-taker-in-bangalore-bengaluru/p/1'
    ]
    pno = 2

    def parse(self, response):
        items = AmazonItem()

        products = response.css(".list-iteme")
        for product in products:
            name = product.css(".list-textdiv .btn_preview").css("::text").extract_first()
            location = product.css("small:nth-child(1) span").css("::text").extract_first()
            t = product.css(".list-specialitiesdiv~ .list-specialitiesdiv+ .list-specialitiesdiv p").css("::text").extract()
            tag = ""
            for i in t:
                if i == '\r\n':
                    pass
                else:
                    tag = tag + i + ","
            print(tag)

            # getitby = product.css(".s-align-children-center .a-text-bold").css("::text").extract_first()
            # stars = product.css(".aok-align-bottom .a-icon-alt").css("::text").extract_first()
            # image = product.css(".s-image::attr(src)").extract_first()

            items["name"] = name
            items["location"] = location
            items["tag"] = tag
            # items["getitby"] = getitby
            # items["stars"] = stars
            # items["image"] = image

            yield items

        next_page = "https://www.bookmybai.com/hire-full-time-maid-and-elderly-care-taker-in-bangalore-bengaluru/p/"+str(ZonSpider.pno)
        if ZonSpider.pno <=5:
            ZonSpider.pno += 1
            yield response.follow(next_page, callback=self.parse)