import matplotlib.pyplot as plt


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
gastos_diesel = [10263.73, 7471.75, 11680.30, 10082.08, 10716.57, 9924.94, 8931.75, 9047.70, 4283.30, 10100.31, 6616.63, 9984.88]

plt.figure(figsize=(8, 6))
plt.pie(gastos_diesel, labels=meses, autopct='%1.1f%%', startangle=90)
plt.title("Gastos de Diesel por Mês")
plt.axis('equal') 

plt.savefig('pizza.png')  
plt.show()

consumo_km_litro = 2.33  
preco_diesel = 2.60  
distancia_mensal_km = 5000 

litros_mensais_por_caminhao = distancia_mensal_km / consumo_km_litro

gasto_mensal_por_caminhao = litros_mensais_por_caminhao * preco_diesel

numero_caminhoes = 220
gasto_anual_total = gasto_mensal_por_caminhao * 12 * numero_caminhoes

print(f"Gasto anual de diesel para toda a frota: R$ {gasto_anual_total:.2f}")

import matplotlib.pyplot as plt

consumo_km_litro = 2.33  
preco_diesel = 2.60  
distancia_mensal_km = 5000  
numero_caminhoes = 220  


litros_mensais_por_caminhao = distancia_mensal_km / consumo_km_litro


gasto_mensal_por_caminhao = litros_mensais_por_caminhao * preco_diesel


gasto_anual_total = gasto_mensal_por_caminhao * 12 * numero_caminhoes


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
gastos_mensais = [gasto_mensal_por_caminhao] * 12


plt.figure(figsize=(10, 6))
plt.bar(meses, gastos_mensais)
plt.xlabel("Mês")
plt.ylabel("Gasto de Diesel")
plt.title("Gasto Mensal de Diesel para a Frota de 220 Caminhões")
plt.grid(axis="y")

# Exibe o gráfico
plt.show()

print(f"Gasto anual de diesel para toda a frota: R$ {gasto_anual_total:.2f}")