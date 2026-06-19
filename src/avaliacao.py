import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from config import FIGURES_DIR

from pathlib import Path
from utils.logger import get_logger

print(__file__)

logger = get_logger(__name__)




def grafico_real_vs_previsto(
    y_test: pd.Series,
    predicoes
):
    """
    Gera gráfico de dispersão entre valores reais e previstos.
    Também plota a linha ideal (y=x) e uma linha de tendência.
    """

    logger.info("Gerando gráfico de Valores Reais x Valores Previstos")

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        predicoes,
        alpha=0.7,
        label="Previsões"
    )

    minimo = min(y_test.min(), predicoes.min())
    maximo = max(y_test.max(), predicoes.max())

    # Linha ideal
    plt.plot(
        [minimo, maximo],
        [minimo, maximo],
        color="red",
        linestyle="--",
        linewidth=2,
        label="Linha Ideal (y=x)"
    )

    # Linha de tendência
    coef = np.polyfit(y_test, predicoes, 1)
    tendencia = np.poly1d(coef)

    plt.plot(
        y_test,
        tendencia(y_test),
        color="green",
        linewidth=2,
        label="Linha de Tendência"
    )

    plt.title("Valores Reais x Valores Previstos")

    plt.xlabel("Valores Reais")

    plt.ylabel("Valores Previstos")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "real_vs_previsto.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logger.info("Gráfico salvo com sucesso.")


def grafico_residuos(
    y_test: pd.Series,
    predicoes
):
    """
    Gera gráfico dos resíduos.
    """

    logger.info("Gerando gráfico de resíduos")

    residuos = y_test - predicoes

    plt.figure(figsize=(8,6))

    plt.scatter(
        predicoes,
        residuos,
        alpha=0.7
    )

    plt.axhline(
        y=0,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Erro Zero"
    )

    plt.title("Gráfico dos Resíduos")

    plt.xlabel("Valores Previstos")

    plt.ylabel("Resíduo")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "residuos.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logger.info("Gráfico salvo com sucesso.")


def grafico_importancia_variaveis(
    modelo,
    X_train: pd.DataFrame
):
    """
    Gera gráfico de importância das variáveis.
    Funciona apenas para Random Forest.
    """

    if not hasattr(modelo, "feature_importances_"):
        logger.warning(
            "Modelo não possui feature_importances_."
        )
        return

    logger.info("Gerando gráfico de importância das variáveis")

    importancia = pd.Series(
        modelo.feature_importances_,
        index=X_train.columns
    )

    importancia = importancia.sort_values()

    plt.figure(figsize=(9,6))

    importancia.plot(kind="barh")

    plt.title("Importância das Variáveis")

    plt.xlabel("Importância")

    plt.grid(True, axis="x")

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "importancia_variaveis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logger.info("Gráfico salvo com sucesso.")


def grafico_distribuicao_residuos(
    y_test: pd.Series,
    predicoes
):
    """
    Histograma da distribuição dos resíduos.
    """

    logger.info("Gerando histograma dos resíduos")

    residuos = y_test - predicoes

    plt.figure(figsize=(8,6))

    plt.hist(
        residuos,
        bins=25
    )

    plt.title("Distribuição dos Resíduos")

    plt.xlabel("Resíduo")

    plt.ylabel("Frequência")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "histograma_residuos.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logger.info("Gráfico salvo com sucesso.")


def gerar_avaliacao(
    modelo,
    X_train,
    y_test,
    predicoes
):
    """
    Executa toda a avaliação gráfica do modelo.
    """

    print("entrou em gerar_avaliação")
    print(FIGURES_DIR)
    print(FIGURES_DIR.exists())
    logger.info("Iniciando avaliação gráfica")

    grafico_real_vs_previsto(
        y_test,
        predicoes
    )

    grafico_residuos(
        y_test,
        predicoes
    )

    grafico_importancia_variaveis(
        modelo,
        X_train
    )

    grafico_distribuicao_residuos(
        y_test,
        predicoes
    )

    logger.info("Avaliação gráfica concluída.")