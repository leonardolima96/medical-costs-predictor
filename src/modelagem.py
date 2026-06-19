import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from utils.logger import get_logger

logger = get_logger(__name__)

def treinar_regressao(X_train, y_train):
    logger.info("Treinando modelo de Regressão Linear")
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    logger.info("Modelo treinado com sucesso!")
    
    return modelo

def treinar_random_forest(X_train, y_train):
    logger.info("Treinando modelo de Random Forest")
    modelo = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    
    modelo.fit(X_train, y_train)
    logger.info("Modelo treinado com sucesso!")
    
    return modelo

def avaliar_modelo(modelo, X_test, y_test):
    logger.info("Iniciando avaliação do modelo preditivo")
    predicoes = modelo.predict(X_test)
    
    mae = mean_absolute_error(y_test, predicoes)
    rmse = root_mean_squared_error(y_test, predicoes)
    r2 = r2_score(y_test, predicoes)
    logger.info("Avaliação concluída!")
    
    return{
        "Modelo": type(modelo).__name__,
        "MAE": round(mae,2),
        "RMSE": round(rmse,2),
        "R²": round(r2,2),
        "Predições": predicoes
    }
    
def comparar_modelos(resultado_linear: dict, resultado_rf: dict, modelo_linear, modelo_rf):
    logger.info("Comparando desempenho dos modelos.")

    print("\n" + "=" * 70)
    print(f"{'Modelo':<25}{'MAE':>12}{'RMSE':>12}{'R²':>10}")
    print("-" * 70)

    print(
        f"{resultado_linear['Modelo']:<25}"
        f"{resultado_linear['MAE']:>12.2f}"
        f"{resultado_linear['RMSE']:>12.2f}"
        f"{resultado_linear['R²']:>10.2f}"
    )

    print(
        f"{resultado_rf['Modelo']:<25}"
        f"{resultado_rf['MAE']:>12.2f}"
        f"{resultado_rf['RMSE']:>12.2f}"
        f"{resultado_rf['R²']:>10.2f}"
    )

    print("=" * 70)

    if resultado_linear["R²"] > resultado_rf["R²"]:
        melhor_modelo = modelo_linear
        melhor_resultado = resultado_linear
    else:
        melhor_modelo = modelo_rf
        melhor_resultado = resultado_rf

    logger.info(f"Melhor modelo: {melhor_resultado["Modelo"]}")
    print(f"\n🏆 Melhor modelo: {melhor_resultado["Modelo"]}")

    return melhor_modelo, melhor_resultado

def executar_modelagem(X_train,X_test, y_train, y_test):
    logger.info("Iniciando modelagem")
    modelo_linear = treinar_regressao(X_train, y_train)
    
    resultado_linear = avaliar_modelo(
        modelo_linear,
        X_test,
        y_test
    )
    
    modelo_rf = treinar_random_forest(X_train, y_train)
    
    resultado_rf = avaliar_modelo(
        modelo_rf,
        X_test,
        y_test
    )
    
    melhor_modelo, melhor_resultado = comparar_modelos(
        resultado_linear,
        resultado_rf,
        modelo_linear,
        modelo_rf)

    
    logger.info("Modelagem Concluída")
    return melhor_modelo, melhor_resultado

