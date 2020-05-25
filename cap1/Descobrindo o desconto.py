
# coding: utf-8

# In[1]:


valor = float(input("Informe o valor do produto:\nR$ "))
promocao = float(input("Informe o valor do produto na promoção:\nR$ "))
X = promocao * 100 / valor
desconto = 100 - X
print("O desconto foi de", str(desconto)+"%")


