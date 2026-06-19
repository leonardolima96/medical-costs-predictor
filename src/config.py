from pathlib import Path

# Raíz do Projeto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Diretórios Principais
DATA_DIR = ROOT_DIR / "data"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

LOG_DIR = ROOT_DIR / "logs"

SRC_DIR = ROOT_DIR / "src"

# Arquivos 

INSURANCE_FILE = BRONZE_DIR / "insurance.csv"
EDA_REPORT = LOG_DIR / "eda_report.txt"
SILVER_FILE = SILVER_DIR / "insurance_tratado.csv"

TREATMENT_REPORT = LOG_DIR / "treatment_report.txt"

