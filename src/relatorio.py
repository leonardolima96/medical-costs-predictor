from pathlib import Path
from datetime import datetime
from config import PDF_REPORT, FIGURES_DIR

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from utils.logger import get_logger

logger = get_logger(__name__)



def gerar_relatorio(metricas: dict):
    """
    Gera um relatório PDF contendo as métricas e os gráficos
    produzidos durante a avaliação do modelo.
    """

    print("entrou em gerar relatório")
    logger.info("Gerando relatório em PDF.")

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(str(PDF_REPORT))

    elementos = []

    # ==========================================================
    # Título
    # ==========================================================

    elementos.append(
        Paragraph(
            "<b>Relatório de Avaliação do Modelo Preditivo</b>",
            styles["Title"]
        )
    )

    elementos.append(Spacer(1, 20))

    # ==========================================================
    # Projeto
    # ==========================================================

    elementos.append(
        Paragraph(
            "<b>Projeto:</b> Predição de Custos Médicos utilizando Machine Learning",
            styles["Heading2"]
        )
    )

    elementos.append(Spacer(1, 12))

    # ==========================================================
    # Modelo
    # ==========================================================

    elementos.append(
        Paragraph(
            f"<b>Modelo Selecionado:</b> {metricas['Modelo']}",
            styles["Heading2"]
        )
    )

    elementos.append(Spacer(1, 15))

    # ==========================================================
    # Métricas
    # ==========================================================

    elementos.append(
        Paragraph("<b>Métricas de Avaliação</b>", styles["Heading2"])
    )

    elementos.append(
        Paragraph(f"MAE: {metricas['MAE']}", styles["BodyText"])
    )

    elementos.append(
        Paragraph(f"RMSE: {metricas['RMSE']}", styles["BodyText"])
    )

    elementos.append(
        Paragraph(f"R²: {metricas['R²']}", styles["BodyText"])
    )

    elementos.append(Spacer(1, 20))

    # ==========================================================
    # Interpretação
    # ==========================================================

    interpretacao = f"""
    O modelo selecionado foi <b>{metricas['Modelo']}</b>,
    apresentando um coeficiente de determinação (R²) igual a
    <b>{metricas['R²']}</b>.
    Isso indica boa capacidade de explicar a variação dos custos
    médicos presentes no conjunto de dados.

    O erro absoluto médio (MAE) foi de
    <b>{metricas['MAE']}</b>,
    enquanto o erro quadrático médio (RMSE) foi
    <b>{metricas['RMSE']}</b>,
    indicando desempenho consistente para fins preditivos.
    """

    elementos.append(
        Paragraph(
            "<b>Interpretação</b>",
            styles["Heading2"]
        )
    )

    elementos.append(
        Paragraph(
            interpretacao,
            styles["BodyText"]
        )
    )

    elementos.append(Spacer(1, 25))

    # ==========================================================
    # Gráficos
    # ==========================================================

    elementos.append(
        Paragraph(
            "<b>Gráficos Gerados</b>",
            styles["Heading2"]
        )
    )

    figuras = [
        ("Valores Reais x Previstos", "real_vs_previsto.png"),
        ("Resíduos", "residuos.png"),
        ("Distribuição dos Resíduos", "histograma_residuos.png"),
        ("Importância das Variáveis", "importancia_variaveis.png")
    ]

    for titulo, arquivo in figuras:

        caminho = FIGURES_DIR / arquivo

        if caminho.exists():

            elementos.append(
                Paragraph(
                    f"<b>{titulo}</b>",
                    styles["Heading3"]
                )
            )

            elementos.append(Spacer(1, 5))

            elementos.append(
                Image(
                    str(caminho),
                    width=450,
                    height=320
                )
            )

            elementos.append(Spacer(1, 20))

    # ==========================================================
    # Conclusão
    # ==========================================================

    conclusao = """
    O modelo apresentou desempenho satisfatório para previsão de
    custos médicos, podendo ser utilizado como ferramenta de apoio
    à tomada de decisão em contextos relacionados a seguros de saúde.
    Entretanto, os resultados não substituem análises clínicas ou
    atuariais especializadas e dependem das variáveis disponíveis
    no conjunto de dados.
    """

    elementos.append(
        Paragraph(
            "<b>Conclusão</b>",
            styles["Heading2"]
        )
    )

    elementos.append(
        Paragraph(
            conclusao,
            styles["BodyText"]
        )
    )

    elementos.append(Spacer(1, 20))

    # ==========================================================
    # Rodapé
    # ==========================================================

    elementos.append(
        Paragraph(
            f"Relatório gerado automaticamente pela pipeline em "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            styles["Italic"]
        )
    )

    doc.build(elementos)

    logger.info("Relatório PDF gerado com sucesso.")