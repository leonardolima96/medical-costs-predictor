import pandas as pd
from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)


def carregar_dados(caminho: Path) -> pd.DataFrame:
   logger.info(f"Iniciando leitura do arquivo: {caminho}")
   if not caminho.exists():
        logger.error(f"Arquivo não encontrado: {caminho}")
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
   try:
        df = pd.read_csv(caminho)
        logger.info(f"Arquivo carregado com sucesso. Registros: {len(df)}")
        
        return df
        
   except Exception:
        logger.exception(f"Erro ao carregar o arquivo: {caminho}")
        raise
    

