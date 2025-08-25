# tests/test_main.py
import json
from typer.testing import CliRunner
from main import app

class ProvedorDeCotacaoFalso:
    def buscar_cotacao_atual(self) -> float:

        return 5.25
    
runner = CliRunner()

def test_converter_com_sucesso(mocker):

    mocker.patch(
        "main.ProvedorDeCotacaoAPI",
        ProvedorDeCotacaoFalso
    )

    result = runner.invoke(app, ["10"])

    assert result.exit_code == 0

    log_lines = result.stdout.strip().split('\n')
    ultimo_log_str = log_lines[-1]
    log_data = json.loads(ultimo_log_str)

    assert log_data["event"] == "Conversão realizada com sucesso"
    assert log_data["valor_em_real"] == "52.50"