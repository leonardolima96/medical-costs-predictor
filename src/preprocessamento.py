import pandas as pd
from sklearn.model_selection import train_test_split
from utils.logger import get_logger

logger = get_logger(__name__)





def codificar_variaveis(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando codificação de variáveis categóricas")
    df['sex'] = df['sex'].map({
        "male" : 1,
        "female": 0
    })
    df["smoker"] = df["smoker"].map({
        "yes": 1,
        "no": 0
    })
    
    df = pd.get_dummies(
        df,
        columns=["region"],
        drop_first=True,
        dtype=int
    )

    return df

def separar_features_target(df: pd.DataFrame):
    logger.info("Iniciando separação de variáveis alvo e independentes")
    X = df.drop(columns="charges")
    y = df["charges"]
    
    return X, y

def dividir_treino_teste(X, y):
    logger.info("Iniciando divisão de treino/teste")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    return X_train, X_test, y_train, y_test

def preprocessar(df):
    logger.info("Iniciando pré-processamento de dados")
    df = codificar_variaveis(df)
    X,y = separar_features_target(df)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X,y)
    logger.info("Pré-processamento concluído")
    
    return X_train, X_test, y_train, y_test

    