import random
class Perceptron:
    def __init__(self, w1, w2, umbral, tasa):
        self.w1 = w1  # Peso para la primera entrada
        self.w2 = w2  # Peso para la segunda entrada
        self.umbral = umbral    # Umbral (sesgo, Angulo)
        self.tasa = tasa    # Tasa de aprendizaje(lambda)
        self.errorPromedioEntrenamiento = 100


    def entrenar(self, entradas1, entradas2, salidaDeseadas):
        self.errorPromedioEntrenamiento = 0
        cantidadEntradas = len(entradas1)
        for i in range(len(entradas1)):
            entrada1 = entradas1[i]
            entrada2 = entradas2[i]
            salidaDeseada = salidaDeseadas[i]

            # Calcular z
            net = entrada1 * self.w1 + entrada2 * self.w2 - self.umbral

            # Calcular la Activacion
            salida = 0
            if net >= 0:
                salida = 1

            # Calcular el e
            error = salidaDeseada - salida

            # Actualizar nuevos pesos
            self.w1 += self.tasa * error * entrada1
            self.w2 += self.tasa * error * entrada2
            self.umbral -= self.tasa * error
            
            self.errorPromedioEntrenamiento += abs(self.calculoError(salida,salidaDeseada))
        #self.errorPromedioEntrenamiento = self.errorPromedioEntrenamiento / cantidadEntradas
        self.errorPromedioEntrenamiento /= cantidadEntradas #jajaja si jala
        

    
    def calculoError(self, salida, salidaDeseada):
        #Calculo del error en porcentaje
        if(salidaDeseada != 0):
            return (salida - salidaDeseada)/salidaDeseada * 100
        else: 
            return (salida - salidaDeseada)*100

    def predecir(self, entrada1, entrada2):
        # Calcular el resultado neto
        net = entrada1 * self.w1 + entrada2 * self.w2 - self.umbral
        
        # Calcular la salida
        if net >= 0:
            return 1
        else:
            return 0        


# Valores iniciales, Pueden ser aleatorios tambien o fijos
'''
tasa = 0.2
w1 = 0.2
w2 = 0.6
umbral = 0.4
'''
tasa = round(random.random(), 2)
w1 = round(random.random(), 2)
w2 = round(random.random(), 2)
umbral = round(random.random(), 2)

# Datos de entrenamiento
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]

entradas1 = [0,0,1,1] # valores de X1
entradas2 = [0,1,0,1] # valores de X2

salidaDeseadas = [0, 1, 1, 1] # salidas de Y usando OR
salidaDeseadas2 = [0, 0, 0, 1] # salidas de Y usando AND

# Crear perceptron
perceptron = Perceptron(w1, w2, umbral, tasa)

# Entrenar el perceptron
while (perceptron.errorPromedioEntrenamiento > 1):
    perceptron.entrenar(entradas1,entradas2, salidaDeseadas2)
    print("Error promedio: ", perceptron.errorPromedioEntrenamiento)


# Mostrar resultados
print("Pesos finales:")
print("w1 =", perceptron.w1)
print("w2 =", perceptron.w2)
print("umbral =", perceptron.umbral)

# Hacer predicciones
print("\nPredicciones:")
for i in range(len(entradas1)):
    salida = perceptron.predecir(entradas1[i], entradas2[i])
    print(entradas1[i], "  ",entradas2[i], "->", salida)
