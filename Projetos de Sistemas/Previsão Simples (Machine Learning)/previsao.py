from sklearn.linear_model import LinearRegression
import numpy as np

#Exemplo: horas jogadas → nota

x = np.array([10],[50],[100])
y = np.array([6],[8],[9])

model = LinearRegression
model.fit(x,y)

previsao = model.predict([[70]])

print("Nota prevista",previsao)