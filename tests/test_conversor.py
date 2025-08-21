# tests/test_conversor.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.conversor import converter_usd_para_brl

def test_conversao_simples():
    
    valor_dolar = 100
    cotacao = 5.0
    valor_esperado = 500.0

    resultado_real = converter_usd_para_brl(valor_dolar, cotacao)
    
    assert resultado_real == valor_esperado