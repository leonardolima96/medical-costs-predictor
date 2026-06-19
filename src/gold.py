
from config import MODEL_METRICS_FILE, MODEL_PREDICTIONS_FILE

import pandas as pd

from utils.logger import get_logger

logger = get_logger(__name__)




def salvar_metricas(metricas: dict):
    """
    Salva as métricas do melhor modelo na camada Gold.
    """

    logger.info("Salvando métricas do modelo.")

    metricas_df = pd.DataFrame([{
        "Modelo": metricas["Modelo"],
        "MAE": metricas["MAE"],
        "RMSE": metricas["RMSE"],
        "R²": metricas["R²"]
    }])

    metricas_df.to_csv(MODEL_METRICS_FILE, index=False)

    logger.info(f"Métricas salvas em: {MODEL_METRICS_FILE}")


def salvar_predicoes(
    y_test: pd.Series,
    predicoes
):
    """
    Salva os valores reais e previstos.
    """

    logger.info("Salvando predições do modelo.")

    predicoes_df = pd.DataFrame({
        "Valor_Real": y_test.values,
        "Valor_Previsto": predicoes
    })

    predicoes_df.to_csv(MODEL_PREDICTIONS_FILE, index=False)

logger.info(f"Predições salvas em: {MODEL_PREDICTIONS_FILE}")


def salvar_gold(
    metricas: dict,
    y_test: pd.Series,
    predicoes
):
    """
    Executa toda a geração da camada Gold.
    """

    print("entrou em salvar gold")
    logger.info("Gerando camada Gold.")

    salvar_metricas(metricas)

    salvar_predicoes(
        y_test,
        predicoes
    )

    logger.info("Camada Gold gerada com sucesso.")