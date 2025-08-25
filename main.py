# main.py
import typer
import sys
import os
import logging
import structlog

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.conversor import converter_usd_para_brl
from infrastructure.ui import exibir_resultado
from infrastructure.cotacao_provider import ProvedorDeCotacaoAPI

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)
log = structlog.get_logger()

app = typer.Typer()

@app.command()
def converter(
    valor_em_dolar: float = typer.Argument(..., help="O valor em dólares a ser convertido.")

):
    """
    Converte um valor de Dólar para Real buscando a cotação atual via API.
    """
    try:
        provedor = ProvedorDeCotacaoAPI()

        cotacao = provedor.buscar_cotacao_atual()
        
        log.info("Iniciando conversão", valor_dolar = valor_em_dolar, cotacao = cotacao)
        valor_em_real = converter_usd_para_brl(valor_em_dolar, cotacao)
        
        exibir_resultado(valor_em_real)
    except ValueError as e:
        log.error("Erro na validação dos dados", detalhe=str(e))
        typer.echo(f"ERRO: Não foi possível realizar a conversão. Detalhe: {e}")


if __name__ == "__main__":
    app()