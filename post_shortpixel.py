import requests
import json

class ShortPixelAPI:
    def __init__(self, key):
        # Sua chave individual da ShortPixel
        self.key = key
        # Url formatada com a chave
        self.url_format = 'https://api.shortpixel.com/v2/post-reducer.php?key=%s' % key

    def upload_imagem(self, imagem_path, nome_imagem):
        data = {
            'key': self.key, 
            'lossy': 0, 
            'file_paths': json.dumps({nome_imagem: imagem_path}),
            'wait': 30
        }
        with open(imagem_path, 'rb') as f:
            files = {nome_imagem: f}
            r = requests.post(
                url=self.url_format,
                data=data,
                files=files
            )
        return r

    def reduzir_tamanho(self, nome_imagem):
        data = {
            'key': self.key, 
            'lossy': 1, 
            'file_names': json.dumps([nome_imagem])
        }
        r = requests.post(
            url=self.url_format,
            data=data
        )
        return r
