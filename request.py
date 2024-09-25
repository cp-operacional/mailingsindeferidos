import requests

# URL da sua API
url = "http://127.0.0.1:8000/indeferidos/"  # Substitua pelo URL correto da sua API

# Dados da requisição
dados = {
    "campos": ["cpf", "nome_completo", "data_nascimento", "municipio", "uf", "especie_beneficio", "competencia_indeferimento", "celular_4"],
    "quantidade": 20,
    "filtros": [
        {
            "uf_municipio": {
                "SC": ["SAO JOSE"],
            },
            "especie_beneficio": [87, 88]
        },
        {
            "uf": ["RS"]
        }
    ]
}

# Fazendo a requisição POST
response = requests.post(url, json=dados)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obtendo o nome do arquivo do cabeçalho Content-Disposition
    content_disposition = response.headers.get('Content-Disposition')
    if content_disposition:
        filename = content_disposition.split('filename=')[1].strip('"')
    else:
        filename = 'indeferidos.xlsx'

    # Salvando o conteúdo da resposta como um arquivo XLSX
    with open(filename, 'wb') as f:
        f.write(response.content)

    print(f"Arquivo '{filename}' baixado com sucesso!")
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)