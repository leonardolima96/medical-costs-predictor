from utils.logger import get_logger
from config import INSURANCE_FILE
from ingestao import carregar_dados

logger = get_logger(__name__)
def main():
    

    logger.info("Iniciando pipeline")

    df = carregar_dados(INSURANCE_FILE)

    logger.info("Pipeline finalizada")
    
    
if __name__ == "__main__":
    main()
    
    