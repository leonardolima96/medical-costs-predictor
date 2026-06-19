from utils.logger import get_logger

from config import INSURANCE_FILE
from ingestao import carregar_dados
from exploracao import explorar_dados
from tratamento import tratar_dados
from preprocessamento import preprocessar
from modelagem import executar_modelagem
from avaliacao import gerar_avaliacao
from relatorio import gerar_relatorio
from gold import salvar_gold

logger = get_logger(__name__)


def main():

    logger.info("=" * 60)
    logger.info("Iniciando pipeline")
    logger.info("=" * 60)

    # ==========================
    # Ingestão
    # ==========================
    df = carregar_dados(INSURANCE_FILE)

    # ==========================
    # Exploração
    # ==========================
    df = explorar_dados(df)

    # ==========================
    # Tratamento
    # ==========================
    df = tratar_dados(df)

    # ==========================
    # Pré-processamento
    # ==========================
    X_train, X_test, y_train, y_test = preprocessar(df)

    # ==========================
    # Modelagem
    # ==========================
    melhor_modelo, metricas = executar_modelagem(
        X_train,
        X_test,
        y_train,
        y_test
    )

    # ==========================
    # Avaliação
    # ==========================
    gerar_avaliacao(
        melhor_modelo,
        X_train,
        y_test,
        metricas["Predições"]
    )

    # ==========================
    # Relatório
    # ==========================
    gerar_relatorio(metricas)
    salvar_gold(
        metricas,
        y_test,
        metricas["Predições"]
    )

    logger.info("=" * 60)
    logger.info("Pipeline finalizada com sucesso!")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()