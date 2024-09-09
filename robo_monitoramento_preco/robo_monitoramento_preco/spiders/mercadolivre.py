from typing import Iterable
import scrapy
from datetime import datetime


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"

    def start_requests(self):
        urls = ["https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/iphone/iphone-15-pro-max_MODEL_25767840_NoIndex_True"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for elemento in response.xpath("//div[@class='ui-search-result__wrapper']"):
            yield {
                'Nome': elemento.xpath(".//h2[@class='ui-search-item__title']/text()").get(),
                'Data Atual': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'Preço': elemento.xpath(".//div[@class='ui-search-price ui-search-price--size-medium']/div/span/span[2]/text()").get(),
                'Link': elemento.xpath(".//a[@class='ui-search-item__group__element ui-search-link__title-card ui-search-link']/@href").get()
            }
