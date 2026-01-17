import schedule
import time
import subprocess
from time import sleep
import pandas as pd


def run_spider():
    with open('spider_log.txt', 'w') as log_file:
        try:
            subprocess.run(['python', 'run_spider.py'],
                           check=True, stdout=log_file, stderr=log_file)
        except subprocess.CalledProcessError as e:
            print(f'Erro ao executar a spider. Verifique spider_log.txt para detalhes.')


def transformar_excel():
    sleep(20)
    csv_file = 'C:\\Users\\rgeba\\OneDrive\\Documentos\\CURSO DEV APRENDER\\Projeto Destrava Web\\Projeto#3 - Robo de Monitoramento de Precos\\robo_monitoramento_preco\\output.csv'
    df = pd.read_csv(csv_file, encoding='utf-8')

    excel_file = 'planilha.xlsx'
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f'Arquivo {csv_file} convertido para {excel_file}')


def job():
    run_spider()
    transformar_excel()


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)
