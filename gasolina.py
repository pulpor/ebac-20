import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha usando o Seaborn
sns.set_style("darkgrid")
sns.lineplot(x='dia', y='preco', data=df)

# Salva o gráfico como uma imagem PNG
plt.savefig('gasolina.png')