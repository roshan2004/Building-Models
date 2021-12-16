import matplotlib.pyplot as plt
import numpy as np
x_vector = np.array([2.47, 0, 0])
y_vector = np.array([0, 4.27, 0])
z_vector = np.array([2.47 * np.cos(60 * np.pi/180), -2.47 * np.sin(60 * np.pi/180), 0])
z1_vector = np.array([-2.47 * np.cos(60 * np.pi/180), -2.47 * np.sin(60 * np.pi/180), 0])
x1 = [np.array([-25.90299988,  48.42700005,   0.27700001])]
for i in range(20):
    x1.append(x1[i] + x_vector)

x2 = [x1[0] + z_vector]
for j in range(17):
    x2.append(x2[j] + x_vector)
    
x3 = [x2[0] + z_vector]
for j in range(17):
    x3.append(x3[j] + x_vector)
    
x4 = [x3[0] + z1_vector]
for j in range(17):
    x4.append(x4[j] + x_vector)
x5 = [x4[0] + z1_vector]
for j in range(17):
    x5.append(x5[j] + x_vector)
    
x6 = [x5[0] + z_vector]
for j in range(17):
    x6.append(x6[j] + x_vector)

x7 = [x6[0] + z_vector]
for j in range(17):
    x7.append(x7[j] + x_vector)
    
x8 = [x7[0] + z1_vector]
for j in range(17):
    x8.append(x8[j] + x_vector)
x9 = [x8[0] + z1_vector]
for j in range(17):
    x9.append(x9[j] + x_vector)
    
    
x10 = [x9[0] + z_vector]
for j in range(17):
    x10.append(x10[j] + x_vector)
    
x11 = [x10[0] + z_vector]
for j in range(17):
    x11.append(x11[j] + x_vector)
    
x12 = [x11[0] + z1_vector]
for j in range(17):
    x12.append(x12[j] + x_vector)
x13 = [x12[0] + z1_vector]
for j in range(17):
    x13.append(x13[j] + x_vector)
    
x14 = [x13[0] + z_vector]
for j in range(17):
    x14.append(x14[j] + x_vector)

x15 = [x14[0] + z_vector]
for j in range(17):
    x15.append(x15[j] + x_vector)
    
x16 = [x15[0] + z1_vector]
for j in range(17):
    x16.append(x16[j] + x_vector)
x17 = [x16[0] + z1_vector]
for j in range(17):
    x17.append(x17[j] + x_vector)
    
x18 = [x17[0] + z_vector]
for j in range(17):
    x18.append(x18[j] + x_vector)
    
x19 = [x18[0] + z_vector]
for j in range(17):
    x19.append(x19[j] + x_vector)
    
x20 = [x19[0] + z1_vector]
for j in range(17):
    x20.append(x20[j] + x_vector)
x21 = [x20[0] + z1_vector]
for j in range(17):
    x21.append(x21[j] + x_vector)
    
x22 = [x21[0] + z_vector]
for j in range(17):
    x22.append(x22[j] + x_vector)

x23 = [x22[0] + z_vector]
for j in range(17):
    x23.append(x23[j] + x_vector)
    
x24 = [x23[0] + z1_vector]
for j in range(17):
    x24.append(x24[j] + x_vector)
x25 = [x24[0] + z1_vector]
for j in range(17):
    x25.append(x25[j] + x_vector)
obs= np.array(x1+x2+x3+x4+x5+x6+x7+x8+x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 +
              x20 + x21 + x22 + x23 + x24 + x25)

plt.figure(figsize=(10,8))
plt.plot(obs[:,0], obs[:,1], marker = 'o', linestyle = '')
plt.show()