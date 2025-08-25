# core/conversor.py
from abc import ABC, abstractmethod

class ProvedorDeCotacao(ABC):

    @abstractmethod
    def buscar_cotacao_atual(self) -> float:
        """Busca a cotação atual e a retorna como um float."""
        pass

def converter_usd_para_brl(valor_em_dolar, cotacao):
    if cotacao <= 0:
        raise ValueError("A cotação deve ser um valor positivo.")
    
    return valor_em_dolar * cotacao