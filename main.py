# main.py
import typer
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.conversor import converter_usd_para_brl
from infrastructure.ui import exibir_resultado

app = typer.Typer()

@app.command()
def converter(
    valor_em_dolar: float = typer.Argument(..., help="O valor em dólares a ser convertido."),
    cotacao: float = typer.Option(5.0, "--cotacao", "-c", help="A cotação atual do dólar para a conversão.")
):
    """
    Converte um valor de Dólar para Real com base em uma cotação.
    """
    valor_em_real = converter_usd_para_brl(valor_em_dolar, cotacao)
    exibir_resultado(valor_em_real)


if __name__ == "__main__":
    app()