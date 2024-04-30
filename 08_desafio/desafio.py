import requests
import pandas as pd


def siglas_list():
    response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
    resultado = response.json()
    siglas = []
    for x in resultado:
        siglas.append(x.get('sigla'))
    return siglas


def area_uf(siglas:list):
    area = {}
    for uf in siglas:
        response = requests.get(f'http://servicodados.ibge.gov.br/api/v3/malhas/estados/{uf}/metadados')
        resultado_area = response.json()
        for x in resultado_area:
            area[uf] = x.get('area').get('dimensao')
    
    return area

def cidades_uf(siglas:list):
    cidades = {}
    for uf in siglas:
        response = requests.get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')
        resultado_cidade = response.json()
        cidade_uf = []
        for x in resultado_cidade:
            cidade_uf.append(x.get('nome'))
        
        cidades[uf] = cidade_uf


    return cidades

siglas = siglas_list()

area = area_uf(siglas)
cidades = cidades_uf(siglas)



area_uf_df = pd.DataFrame(list(area.items()), columns=['uf', 'area'])
area_uf_df.to_csv('./08_desafio/data/csv/uf_area.csv', sep=';', index=False, encoding='utf-8')

cidade_uf_df = pd.DataFrame(list(cidades.items()), columns=['uf', 'cidades'])
cidade_uf_df_separadas = cidade_uf_df.explode('cidades')
cidade_uf_df_separadas.to_parquet('./08_desafio/data/parquets/', index=False, partition_cols=['uf'])