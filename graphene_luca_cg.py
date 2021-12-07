import matplotlib.pyplot as plt
import numpy as np
x_vector = np.array([2.47, 0, 0])
y_vector = np.array([0, 4.27, 0])
z_vector = np.array([2.47 * np.cos(60 * np.pi/180), 2.47 * np.sin(60 * np.pi/180), 0])

x1 = [np.array([0,0,0])]
for i in range(5):
    x1.append(x1[i] + x_vector) 
    
x2 = [x1[0] + z_vector]
for j in range(4):
    x2.append(x2[j] + x_vector)
    
x3 = [x1[0] + y_vector]
for k in range(5):
    x3.append(x3[k] + x_vector)
x4 = [x3[0] + z_vector]
for l in range(4):
    x4.append(x4[l] + x_vector)

obs = np.unique(np.array(x1 + x2 + x3 + x4), axis = 0)

plt.figure(figsize=(10,8))
plt.plot(obs[:,0], obs[:,1], marker = 'o', linestyle = '')
plt.show()