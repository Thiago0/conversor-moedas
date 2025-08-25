# infrastructure/ui.py
import structlog

log = structlog.get_logger()

def exibir_resultado(valor_em_real):
    log.info("Conversão realizada com sucesso", valor_em_real=f"{valor_em_real:.2f}")