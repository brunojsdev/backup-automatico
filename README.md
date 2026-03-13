# Backup Automático

## Descrição
Utilitário simples e eficiente para criar backups compactados (.zip) de diretórios importantes. Cada arquivo de backup recebe um timestamp no nome para facilitar o controle de versão e evitar a perda de dados.

## Funcionalidades
- Compactação automática de diretórios inteiros preservando a estrutura interna de pastas.
- Nomenclatura baseada em data e hora (Ex: backup_pasta_20231025_153000.zip).
- Criação automática da pasta de destino caso ela não exista.

## Pré-requisitos
- Python 3.x
- Bibliotecas padrão do Python (os, zipfile, datetime, pathlib). Nenhuma instalação externa é necessária.

## Como Usar
1. Execute o script.
2. Forneça o caminho da pasta de origem (a pasta que será copiada).
3. Forneça o caminho da pasta de destino (onde o arquivo .zip será guardado).
