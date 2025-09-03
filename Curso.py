import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_treinamento = [
  [1.0 , 2.0 , "A"],
  [2.0 , 3.0 , "A"],
  [3.0 , 3.0 , "B"],
  [2.0 , 1.0 , "B"]
]

colunas = ["X", "Y", "classe"]
tabela = pd.DataFrame(dados_treinamento, columns=colunas)
ponto_alvo = pd.DataFrame([[2.5, 1.5, '']], columns=colunas)

print(tabela)

# função distância 
def distancia(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Descobrir todas as classes presentes nos dados de treinamento
classes = tabela['classe'].unique()


# Para cada classe, desenhar os pontos em uma cor diferente

for c in classes:
  pontos_da_classe = tabela[tabela['classe'] == c]
  plt.scatter(pontos_da_classe['X'], pontos_da_classe['Y'], label = c)

plt.scatter(ponto_alvo['X'], ponto_alvo['Y'], marker='X', label = "Ponto Alvo")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Dispersão")
plt.legend()
plt.show()

dsitancia = []

for c in range(len(tabela.values)):
  di = distancia(ponto_alvo.values[0][0], ponto_alvo.values[0][1], tabela.values[c][0], tabela.values[c][1])
  dsitancia.append(di)

vizinho = np.argmin(distancia)
classe = tabela['classe'][vizinho]
print("O exemplo pertence a classe: " + str(classe))