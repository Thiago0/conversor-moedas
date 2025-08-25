#infrastructure/cotacao_provider.py
import requests

from core.conversor import ProvedorDeCotacao


class ProvedorDeCotacaoAPI(ProvedorDeCotacao):

    def buscar_cotacao_atual(self) -> float:
        """
        Busca a cotação atual do Dólar para Real usando uma API pública.
        """
        try:

            response = requests.get("https://economia.awesomeapi.com.br/json/last/last/USD-BRL")
            response.raise_for_status()

            data = response.json()
            cotacao_str = data["USDBRL"]["bid"]

            return float(cotacao_str)
        
        except requests.exceptions.RequestException as e:

            raise RuntimeError(f"Erro ao buscar cotação da API: {e}")