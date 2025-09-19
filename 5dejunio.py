import pandas as pd

class RegistroNotas:
    def __init__(self, archivo):
        self.archivo = archivo
        try:
            self.df = pd.read_csv(archivo)
        except FileNotFoundError:
            print("Archivo no encontrado. Se crea uno vacío.")
            self.df = pd.DataFrame(columns=["nombre", "nota"])

    def mostrar_aprobados(self):
        aprobados = self.df[self.df["Nota"] >= 6.0]
        print("Estudiantes aprobados:")
        print(aprobados)

    def calcular_promedio(self):
        promedio = self.df["Nota"].mean()
        print(f"Promedio general: {promedio:.2f}")
        return promedio

    def buscar_por_nombre(self, nombre):
        resultado = self.df[self.df["Nombre"].str.lower() == nombre.lower()]
        if not resultado.empty:
            print("Estudiante encontrado:")
            print(resultado)
        else:
            print("Estudiante no encontrado.")

    def agregar_estudiante(self, nombre, nota):
        nuevo = pd.DataFrame({"Nombre": [nombre], "Nota": [nota]})
        self.df = pd.concat([self.df, nuevo], ignore_index=True)
        self.df.to_csv(self.archivo, index=False)
        print(f"{nombre} agregado con nota {nota}.")



# ---------------------------
# Ejemplo de uso
# ---------------------------

# Crear instancia con archivo CSV
registro = RegistroNotas("alumnos_notas.csv")

# Mostrar aprobados
registro.mostrar_aprobados()

# Calcular promedio
registro.calcular_promedio()

# Buscar estudiante por nombre
registro.buscar_por_nombre("Ana")

# Agregar nuevo estudiante
registro.agregar_estudiante("Carlos", 4.2)

