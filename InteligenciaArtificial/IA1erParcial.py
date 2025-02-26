import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Problema 1: Análisis y Manipulación de Datos
# Se espera un archivo CSV con ventas

def analizar_ventas(csv_file):
    df = pd.read_csv(csv_file)
    df.dropna(inplace=True)
    df['Venta_Total'] = df['Cantidad'] * df['Precio']
    print("Producto con mayor venta total:", df.groupby('Producto')['Venta_Total'].sum().idxmax())
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df.groupby(pd.Grouper(key='Fecha', freq='M'))['Venta_Total'].sum().plot(kind='line', marker='o')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas Totales')
    plt.title('Evolución de Ventas Totales')
    plt.show()

# Problema 2: Modelo de Clasificación con Iris
def clasificar_iris():
    from sklearn.datasets import load_iris
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Problema 3: Manejo de Datos Faltantes y Selección de Características
def manejar_datos(csv_file):
    df = pd.read_csv(csv_file)
    df.fillna(df.mean(), inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    print("Correlación con variable objetivo:", df.corr()['Compra'].sort_values(ascending=False))

# Problema 4: Optimización de Hiperparámetros con GridSearchCV
def optimizar_modelo():
    from sklearn.datasets import load_iris
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', RandomForestClassifier())
    ])
    param_grid = {
        'clf__n_estimators': [50, 100, 200],
        'clf__max_depth': [None, 10, 20, 30]
    }
    grid = GridSearchCV(pipeline, param_grid, cv=5)
    grid.fit(X_train, y_train)
    print("Mejores parámetros:", grid.best_params_)
    print("Accuracy en test:", grid.score(X_test, y_test))

if __name__ == "__main__":
    print("Ejecute las funciones con los archivos correspondientes.")
