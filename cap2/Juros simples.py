
# coding: utf-8

# In[1]:


c = float(input("Informe o valor da compra:\nR$ "))
i = float(input("Informe o percentual da taxa de juros:\n"))
J = c * (i/100) * 2
valor_pago = c+J
print("Valor acrescido dos juros R$", valor_pago)


