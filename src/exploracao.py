from datetime import datetime

import pandas as pd

from config import EDA_REPORT
from utils.logger import get_logger

logger = get_logger(__name__)

SEPARADOR = "=" * 70


def explorar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza uma análise exploratória inicial do DataFrame e gera
    um relatório em formato .txt.

    Args:
        df: DataFrame contendo os dados carregados.

    Returns:
        O mesmo DataFrame recebido.
    """

    logger.info("Iniciando análise exploratória dos dados.")

    try:
        with open(EDA_REPORT, "w", encoding="utf-8") as arquivo:

            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write("RELATÓRIO DE ANÁLISE EXPLORATÓRIA (EDA)\n")
            arquivo.write(f"{SEPARADOR}\n\n")

            arquivo.write(
                f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            )

            # ===============================
            # Dimensão
            # ===============================
            arquivo.write("DIMENSÃO DO DATASET\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"Linhas: {df.shape[0]}\n")
            arquivo.write(f"Colunas: {df.shape[1]}\n\n")

            # ===============================
            # Tipos das colunas
            # ===============================
            arquivo.write("TIPOS DAS COLUNAS\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"{df.dtypes}\n\n")

            # ===============================
            # Valores nulos
            # ===============================
            arquivo.write("VALORES NULOS\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"{df.isnull().sum()}\n\n")

            # ===============================
            # Registros duplicados
            # ===============================
            arquivo.write("REGISTROS DUPLICADOS\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"{df.duplicated().sum()}\n\n")

            # ===============================
            # Uso de memória
            # ===============================
            memoria_mb = df.memory_usage(deep=True).sum() / 1024**2

            arquivo.write("USO DE MEMÓRIA\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"{memoria_mb:.2f} MB\n\n")

            # ===============================
            # Estatísticas
            # ===============================
            arquivo.write("ESTATÍSTICAS DESCRITIVAS\n")
            arquivo.write(f"{SEPARADOR}\n")
            arquivo.write(f"{df.describe(include='all')}\n")

        logger.info("Relatório EDA gerado com sucesso.")

    except Exception:
        logger.exception("Erro ao gerar o relatório de análise exploratória.")
        raise

    return df