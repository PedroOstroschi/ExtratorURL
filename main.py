from ExtratorURL import ExtratorURL

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DESTINO = 1/5.50  # 1 moeda de origem = 5.50 moeda de destino
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

quantide_final = int(quantidade) * VALOR_DESTINO

print("{} {}".format(quantide_final, moeda_destino))