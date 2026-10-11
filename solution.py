from datetime import datetime, timedelta
import requests

def cotar():
    """
    Função que retorna uma lista com a cotação de compra do dólar 
    para os últimos 365 dias, começando do dia atual.
    """
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/365"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacoes = [float(item['bid']) for item in dados]
        return cotacoes
    except Exception as e:
        print(f"Erro ao buscar cotações: {e}")
        return []

if __name__ == "__main__":
    resultado = cotar()
    print(resultado)
