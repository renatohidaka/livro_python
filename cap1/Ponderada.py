
# coding: utf-8

# In[1]:


x1 = float(input("Informe o primeiro valor:\n"))
x2 = float(input("Informe o segundo valor:\n"))
p1 = 3.5
p2 = 7.5
M = (x1*p1 + x2*p2) / (p1+p2)
M = str('%.2f'%M)
print("Média ponderada é =", M)


