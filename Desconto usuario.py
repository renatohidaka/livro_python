
# coding: utf-8

# In[1]:


valor = float(input("Informe o valor do produto:\nR$ "))
percentual = int(input("Informe o percentual do desconto:\n"))
desconto = valor * percentual / 100
valor_final = valor - desconto
print("Valor do produto com", str(percentual)+"%", "de desconto é de R$", valor_final)

