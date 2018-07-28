from urllib import request

url_public = 'https://app.rdstation.com.br/leads/public/09c2f091-90b6-4654-a900-a28968ec7332'

with request.urlopen(url_public) as response:
    html = response.read().decode('utf8')

print(html)
