url = "https://bytebank.com/cambio?moedaOrigem=real"
# http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)