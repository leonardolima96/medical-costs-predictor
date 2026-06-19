from datetime import datetime

import pandas as pd

from config import SILVER_FILE, TREATMENT_REPORT
from utils.logger import get_logger

logger = get_logger(__name__)

SEPARADOR = "=" * 70


def remover_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove registros duplicados do DataFrame.

    Args:
        df: DataFrame original.

    Returns:
        DataFrame sem registros duplicados.
    """

    linhas_antes = len(df)

    df = df.drop_duplicates()

    linhas_depois = len(df)

    removidos = linhas_antes - linhas_depois

    logger.info(f"{removidos} registro(s) duplicado(s) removido(s).")

    return df


def salvar_silver(df: pd.DataFrame) -> None:
    """
    Salva o DataFrame tratado na camada Silver.

    Args:
        df: DataFrame tratado.
    """

    df.to_csv(SILVER_FILE, index=False)

    logger.info(f"Dataset salvo em: {SILVER_FILE}")


def gerar_relatorio_tratamento(
    linhas_antes: int,
    linhas_depois: int,
    duplicados_removidos: int,
) -> None:
    """
    Gera um relatório TXT com o resumo do tratamento realizado.
    """

    with open(TREATMENT_REPORT, "w", encoding="utf-8") as arquivo:

        arquivo.write(f"{SEPARADOR}\n")
        arquivo.write("RELATÓRIO DE TRATAMENTO DOS DADOS\n")
        arquivo.write(f"{SEPARADOR}\n\n")

        arquivo.write(
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
        )

        arquivo.write(f"Registros antes do tratamento : {linhas_antes}\n")
        arquivo.write(f"Registros após o tratamento   : {linhas_depois}\n")
        arquivo.write(f"Duplicados removidos          : {duplicados_removidos}\n")
        arquivo.write("Valores nulos tratados        : 0\n")
        arquivo.write(f"\nArquivo salvo em:\n{SILVER_FILE}\n")

        arquivo.write(f"\n{SEPARADOR}\n")
        arquivo.write("FIM DO RELATÓRIO\n")
        arquivo.write(f"{SEPARADOR}\n")

    logger.info("Relatório de tratamento gerado com sucesso.")


def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa todas as etapas de tratamento dos dados.

    Args:
        df: DataFrame original.

    Returns:
        DataFrame tratado.
    """

    logger.info("Iniciando tratamento dos dados.")

    linhas_antes = len(df)

    df = remover_duplicados(df)

    linhas_depois = len(df)

    duplicados_removidos = linhas_antes - linhas_depois

    salvar_silver(df)

    gerar_relatorio_tratamento(
        linhas_antes,
        linhas_depois,
        duplicados_removidos,
    )

    logger.info("Tratamento dos dados concluído.")

    return df