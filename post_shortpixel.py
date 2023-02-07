import requests
import json

# Sua chave individual da ShortPixel
key = '<sua chave shortpixel>'

# Caminho da imagem
imagem = '<caminho da sua imagem>'

# Nome especifico, utilizado no relatorio
nome_imagem = 'file1'

# Url formatada com a chave
url_format = 'https://api.shortpixel.com/v2/post-reducer.php?key=%s' % key

# Dados enviados pela API com os parametros da documentacao
data = {
   'key': key, 
   'lossy': 0, 
   'file_paths': json.dumps({nome_imagem: imagem}),
   'wait': 30
}

# Request
r = requests.post(
    url=url_format,
    files={nome_imagem: open(imagem, 'rb')},
    data=data)

# Exibicao
print(r.json())
