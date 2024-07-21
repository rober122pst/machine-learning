from ydata_profiling import ProfileReport
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

link = 'https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/d4332a3056f44e1a1dec9600a31f21c8_boston.csv'
planilha = pd.read_csv(link)

print(planilha)

# Criar DataFrame Pandas
data = pd.DataFrame(data=planilha)

#Ver o Data Frame criado
print(data.head())

# Descrever DataFrame
print(data.describe())

profile = ProfileReport(data, title='Relatório - Pandas Profiling', html={'style':{'full_width':True}})

# Checando se há valores nulos
print(data.isnull().sum())

# Correlações
correlacoes = data.corr()

#Grafico
plt.figure(figsize=(16,6))
sns.heatmap(data=correlacoes, annot=True)