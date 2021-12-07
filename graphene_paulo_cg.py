import matplotlib.pyplot as plt
import numpy as np
x_vector = np.array([2.47, 0, 0])
y_vector = np.array([0, 4.27, 0])
z_vector = np.array([2.47 * np.cos(60 * np.pi/180), -2.47 * np.sin(60 * np.pi/180), 0])
z1_vector = np.array([-2.47 * np.cos(60 * np.pi/180), -2.47 * np.sin(60 * np.pi/180), 0])
x1 = [np.array([-25.90299988,  48.42700005,   0.27700001])]
for i in range(4):
    x1.append(x1[i] + x_vector)

x2 = [x1[0] + z_vector]
for j in range(4):
    x2.append(x2[j] + x_vector)
    
x3 = [x2[0] + z_vector]
for j in range(4):
    x3.append(x3[j] + x_vector)
    
x4 = [x3[0] + z1_vector]
for j in range(4):
    x4.append(x4[j] + x_vector)
x5 = [x4[0] + z1_vector]
for j in range(4):
    x5.append(x5[j] + x_vector)
obs= np.array(x1+x2+x3+x4+x5)

plt.figure(figsize=(10,8))
plt.plot(obs[:,0], obs[:,1], marker = 'o', linestyle = '')
plt.show()