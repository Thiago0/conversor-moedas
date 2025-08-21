# main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.conversor import converter_usd_para_brl
from infrastructure.ui import exibir_resultado

if __name__ == "__main__":

    valor_dolar = 100
    contacao_atual = 5.0

    valor_em_real = converter_usd_para_brl(valor_dolar, contacao_atual)

    exibir_resultado(valor_em_real)