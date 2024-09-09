from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from robo_monitoramento_preco.spiders.mercadolivre import MercadolivreSpider


def run_spider():
    try:
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(MercadolivreSpider)
        process.start()
    except Exception as e:
        print(f'Erro ao executar a spider: {e}')


if __name__ == "__main__":
    run_spider()
