from pathlib import Path

# ==========================================
# Diretório raiz
# ==========================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# Dados
# ==========================================
DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

INSURANCE_FILE = BRONZE_DIR / "insurance.csv"
TREATED_DATA_FILE = SILVER_DIR / "insurance_tratado.csv"

MODEL_METRICS_FILE = GOLD_DIR / "model_metrics.csv"
MODEL_PREDICTIONS_FILE = GOLD_DIR / "model_predictions.csv"

# ==========================================
# Outputs
# ==========================================
OUTPUT_DIR = BASE_DIR / "outputs"

FIGURES_DIR = OUTPUT_DIR / "figures"
DOCUMENTS_DIR = OUTPUT_DIR / "documents"

EDA_REPORT = DOCUMENTS_DIR / "eda_report.txt"
TREATMENT_REPORT = DOCUMENTS_DIR / "treatment_report.txt"
PDF_REPORT = DOCUMENTS_DIR / "relatorio_modelo.pdf"

# ==========================================
# Logs
# ==========================================
LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "pipeline.log"

# ==========================================
# Criar diretórios automaticamente
# ==========================================
for pasta in (
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    FIGURES_DIR,
    DOCUMENTS_DIR,
    LOG_DIR,
):
    pasta.mkdir(parents=True, exist_ok=True)