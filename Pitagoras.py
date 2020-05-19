
# coding: utf-8

# In[5]:


xA, yA = map(int, input("Digite as coordenadas x e y do ponto A:\n").split())
xB, yB = map(int, input("Digite as coordenadas x e y do ponto B:\n").split())
X = (xB-xA)**2
Y = (yB-yA)**2
dAB = (X+Y)**0.5
print("A distância entre os dois pontos é =", dAB)


