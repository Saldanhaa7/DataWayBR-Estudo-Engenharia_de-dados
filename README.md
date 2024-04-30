# Curso DataWayBR

Este repositório contém os materiais e projetos desenvolvidos por mim durante o curso da DataWayBR. O curso abordou diversos tópicos relacionados a Python e engenharia de dados. Abaixo está uma breve descrição dos módulos e do projeto final desenvolvido no curso.

## Módulos

### Basics
Neste módulo, revisei operações e funções simples do Python, reforçando conceitos básicos de programação.

### Files
Aprendi a trabalhar com diferentes tipos de arquivos usando Pandas, uma biblioteca Python especializada em manipulação de dados.

### HTTP
Aprendi a fazer diferentes tipos de requisições HTTP, como GET, POST, DELETE e UPDATE, utilizando Python.

### Databases
Neste módulo, aprendi a manipular bancos de dados SQLite e PostgreSQL usando Python.

### Scheduling
Aprendemos sobre agendamento de tarefas com cron e desenvolvemos um monitor de Bitcoin e do hardware do sistema.

### Parquets
Aprendemos a utilizar arquivos Parquet e suas aplicações.

## Projeto Final - Desafio Final

O projeto final do curso foi o Desafio Final, onde trabalhamos com a extração de dados de API de localidades fornecida pelo IBGE. O objetivo foi extrair dados de três APIs:

1. API de Estados: Criamos uma lista de estados do Brasil.
2. API com metadado dos estados: Para cada estado na lista anterior, extraímos a área do estado.
3. API com lista de municípios por estado: Para cada estado na lista, extraímos a lista de municípios.

Ao final do desafio, geramos dois datasets:

1. DATASET 1: Todos os estados do Brasil, e a área de cada estado, ordenados por área (formato CSV).
2. DATASET 2: Um dataset com todos os municípios do Brasil, e a UF a qual pertencem (formato Parquet particionado por UF).


Espero que este repositório possa ser útil para quem está buscando aprender mais sobre Python e engenharia de dados. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.
