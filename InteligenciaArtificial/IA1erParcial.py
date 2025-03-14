import sys, subprocess, os, time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from google.colab import files
from IPython.display import display
from PIL import Image as PILImage    
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


def requisitos():
    libraries = [
        'pandas',
        'matplotlib',
        'sklearn',
        'qrcode',
        'Pillow'
    ]

    for lib in libraries:
        try:
            # Intentamos importar la librería
            __import__(lib)
            print(f"{lib} ya está instalada ✅")
        except ImportError:
            # Si no está instalada, la instalamos
            print(f"Instalando {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"{lib} instalada correctamente ✅")
    
    # Ahora importamos todas las librerías necesarias
    
    print("✅ Todas las librerías han sido importadas correctamente.")

def generar_csvs():
    # p1.csv - Datos de ventas
    data_p1 = pd.DataFrame({
        "Fecha": ["2024-01-01", "2024-01-05", "2024-02-10", "2024-02-15"],
        "Producto": ["ProductoA", "ProductoB", "ProductoA", "ProductoB"],
        "Cantidad": [10, 5, 3, 7],
        "Precio": [20, 50, 20, 50]
    })
    data_p1.to_csv("p1.csv", index=False)
    
    # p2.csv - No se necesita un CSV (datos de sklearn)
    
    # p3.csv - Datos con valores faltantes
    data_p3 = pd.DataFrame({
        "Edad": [25, 30, 35, None, 40],
        "Salario": [50000, None, 60000, 55000, 65000],
        "Compra": [1, 0, 1, 0, 1]
    })
    data_p3.to_csv("p3.csv", index=False)
    
    # p4.csv - No se necesita un CSV (datos de sklearn)

    print("✅ Archivos CSV generados correctamente.")

requisitos()

generar_csvs()

def QR_Generator():
    import qrcode 
    espacio_usuario = get_ipython().user_ns

    try:
        Nombre = espacio_usuario["Nombre"]
        Matricula = espacio_usuario["Matricula"]
        Grupo = espacio_usuario["Grupo"]
    except KeyError as e:
        raise NameError(f"⚠️ La variable '{e.args[0]}' no está definida en el notebook. Asegúrate de ejecutarla antes.") 

    resultados = {}

    try:
        # Prueba para p1 (analizar_ventas)
        analizar_ventas = espacio_usuario["analizar_ventas"]
        try:
            df = pd.read_csv('p1.csv')
            df['Venta_Total'] = df['Cantidad'] * df['Precio']
            venta_total_esperada = df.groupby('Producto')['Venta_Total'].sum().idxmax()
            if venta_total_esperada == analizar_ventas("p1.csv", visible=False):
                resultados["p1_analizar_ventas"] = True
            else:
                resultados["p1_analizar_ventas"] = False
        except Exception:
            resultados["p1_analizar_ventas"] = False

        # Prueba para p2 (clasificar_iris)
        clasificar_iris = espacio_usuario["clasificar_iris"]
        try:
            data = load_iris()
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
            model_ref = LogisticRegression(max_iter=200)
            model_ref.fit(X_train, y_train)
            y_pred_ref = model_ref.predict(X_test)
            acc_ref = accuracy_score(y_test, y_pred_ref)
            if clasificar_iris() >= acc_ref * 0.9:
                resultados["p2_clasificar_iris"] = True
            else: 
                resultados["p2_clasificar_iris"] = False
        except Exception:
            resultados["p2_clasificar_iris"] = False

        # Prueba para p3 (manejar_datos)
        manejar_datos = espacio_usuario["manejar_datos"]
        try:
            df = pd.read_csv('p3.csv')
            df.replace(["NaN", "nan", "None", ""], np.nan, inplace=True)
            df = df.map(lambda x: str(x).strip() if isinstance(x, str) else x)
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            df.fillna(df.mean(numeric_only=True), inplace=True)
            df = pd.get_dummies(df, drop_first=True)
            if 'Compra' in df.columns:
                correlation_test = df.corr()['Compra'].sort_values(ascending=False)
            correlation = manejar_datos("p3.csv")
            if correlation.equals(correlation_test):
                resultados["p3_manejar_datos"] = True
            else:
                resultados["p3_manejar_datos"] = False
        except Exception:
            resultados["p3_manejar_datos"] = False

        # Prueba para p4 (optimizar_modelo)
        optimizar_modelo = espacio_usuario["optimizar_modelo"]
        try:
            data = load_iris()
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
            pipeline_ref = Pipeline([
                ('scaler', StandardScaler()),
                ('clf', RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))
            ])
            pipeline_ref.fit(X_train, y_train)
            param_grid = {
                'clf__n_estimators': [50, 100, 200],
                'clf__max_depth': [None, 10, 20, 30]
            }
            grid_ref = GridSearchCV(pipeline_ref, param_grid, cv=5)
            grid_ref.fit(X_train, y_train)
            best_params_ref = grid_ref.best_params_
            if best_params_ref == optimizar_modelo():
                resultados["p4_optimizar_modelo"] = True
            else:
                resultados["p4_optimizar_modelo"] = False
        except Exception:
            resultados["p4_optimizar_modelo"] = False

    except KeyError as e:
        raise NameError(f"⚠️ La función '{e.args[0]}' no está definida en el notebook.")
    except Exception as e:
        raise RuntimeError(f"⚠️ Error en la ejecución de una función: {e}")

    examen = {
        "datos_alumno": {
            "nombre": Nombre,
            "matricula": Matricula,
            "grupo": Grupo
        },
        "respuestas": resultados,
        "fecha": int(time.time())
    }
    qr = qrcode.make(examen)
    output_filename = "qr_resultados.png"
    qr.save(output_filename)
    print(f"Código QR generado y guardado como {output_filename}")
    files.download('qr_resultados.png')
    img = PILImage.open(output_filename)
    display(img)

class p1(ABC):

    @abstractmethod
    def analizar_ventas(self, csv_file, visible=True):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "analizar_ventas" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'analizar_ventas'.")
            
            funcion_usuario = espacio_usuario["analizar_ventas"]

            # Crear un archivo CSV de prueba
            data = """Fecha,Producto,Cantidad,Precio
            2024-01-01,ProductoA,10,20
            2024-01-05,ProductoB,5,50
            2024-02-10,ProductoA,3,20
            2024-02-15,ProductoB,7,50"""
            
            csv_test = "ventas_test.csv"
            with open(csv_test, "w") as f:
                f.write(data)

            df = pd.read_csv(csv_test)
            df['Venta_Total'] = df['Cantidad'] * df['Precio']
            venta_total_esperada = df.groupby('Producto')['Venta_Total'].sum().idxmax()
            venta_total_calculada = funcion_usuario('p1.csv', visible=False)

            os.remove(csv_test)

            assert venta_total_calculada == venta_total_esperada, "❌ Error en el cálculo de ventas totales."

        except FileNotFoundError:
            print("❌ Error: No se encontró el archivo CSV.")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes crear una función llamada 'analizar_ventas' que reciba un archivo CSV con columnas 'Fecha', 'Producto', 'Cantidad' y 'Precio'.")
        print("La función debe calcular la venta total de cada producto y graficar la evolución mensual de las ventas totales.")

class p2(ABC):

    @abstractmethod
    def clasificar_iris(self):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "clasificar_iris" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'clasificar_iris'.")
            
            funcion_usuario = espacio_usuario["clasificar_iris"]

            data = load_iris()
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

            model_ref = LogisticRegression(max_iter=200)
            model_ref.fit(X_train, y_train)
            y_pred_ref = model_ref.predict(X_test)
            acc_ref = accuracy_score(y_test, y_pred_ref)

            acc_user = funcion_usuario()

            assert acc_user >= acc_ref * 0.9, "❌ La precisión del modelo es significativamente menor de lo esperado."

        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes definir una función llamada 'clasificar_iris' que realice un modelo de clasificación sobre el dataset Iris.")
        print("La función debe dividir los datos en entrenamiento y prueba, entrenar un modelo de Regresión Logística y evaluar su rendimiento con 'accuracy_score' y 'classification_report'.")

class p3(ABC):

    @abstractmethod
    def manejar_datos(self, csv_file):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "manejar_datos" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'manejar_datos'.")
            
            funcion_usuario = espacio_usuario["manejar_datos"]

            # Crear un archivo CSV de prueba
            data = """Edad,Salario,Compra
            25,50000,1
            30,,0
            35,60000,1
            ,55000,0
            40,65000,1"""
            
            csv_test = "datos_test.csv"
            with open(csv_test, "w") as f:
                f.write(data)

            # Leer CSV antes de la ejecución
            df = pd.read_csv(csv_test)
            df.replace(["NaN", "nan", "None", ""], np.nan, inplace=True)
            df = df.map(lambda x: str(x).strip() if isinstance(x, str) else x)
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            df.fillna(df.mean(numeric_only=True), inplace=True)
            df = pd.get_dummies(df, drop_first=True)
            if 'Compra' in df.columns:
                correlation_test = df.corr()['Compra'].sort_values(ascending=False)
            correlation_p3 = funcion_usuario('p3.csv')
            # Ejecutar la función
            #funcion_usuario('p3.csv')

            # Leer CSV después de la ejecución
            #df = pd.read_csv(csv_test)
            #nan_count_after = df.isna().sum().sum()

            # Eliminar el archivo de prueba
            os.remove(csv_test)

            # Assertions
            #assert nan_count_after == 1, f"❌ Error: No se llenaron correctamente los valores nulos.{nan_count_after}"
            #assert "Compra" in df.columns, "❌ Error: La columna 'Compra' no se encuentra en el dataframe."
            assert correlation_p3.equals(correlation_test), "❌ Error: La correlación no corresponde."

        except FileNotFoundError:
            print("❌ Error: No se encontró el archivo CSV.")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes definir una función llamada 'manejar_datos' que reciba un archivo CSV y llene los valores faltantes con la media de la columna.")
        print("También debe convertir las variables categóricas en variables dummy y calcular la correlación con la variable objetivo 'Compra'.")

class p4(ABC):

    @abstractmethod
    def optimizar_modelo(self):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "optimizar_modelo" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'optimizar_modelo'.")
            
            funcion_usuario = espacio_usuario["optimizar_modelo"]

            # Cargar datos y ejecutar la función
            data = load_iris()
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

            # Modelo de referencia para comparación
            pipeline_ref = Pipeline([
                ('scaler', StandardScaler()),
                ('clf', RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))
            ])
            pipeline_ref.fit(X_train, y_train)

            # Entrenar con GridSearchCV para obtener los mejores parámetros
            param_grid = {
                'clf__n_estimators': [50, 100, 200],
                'clf__max_depth': [None, 10, 20, 30]
            }
            grid_ref = GridSearchCV(pipeline_ref, param_grid, cv=5)
            grid_ref.fit(X_train, y_train)
            best_params_ref = grid_ref.best_params_

            assert best_params_ref == funcion_usuario(), "❌ Error: No se encontraron los mejores parámetros del GridSearch."

        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes definir una función llamada 'optimizar_modelo' que entrene un modelo con el dataset Iris utilizando GridSearchCV.")
        print("El modelo debe usar un pipeline con 'StandardScaler' y 'RandomForestClassifier'. Además, debe optimizar los hiperparámetros 'n_estimators' y 'max_depth'.")