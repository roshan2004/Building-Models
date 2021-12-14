import matplotlib.pyplot as plt
import numpy as np
x_vector = np.array([2.47, 0, 0])
y_vector = np.array([0, -4.27, 0])
z_vector = np.array([2.47 * np.cos(60 * np.pi/180), -2.47 * np.sin(60 * np.pi/180), 0])

x1 = [np.array([-25.903,  49.139,   0.277])]
for i in range(21):
    x1.append(x1[i] + x_vector) 
    
x2 = [x1[0] + z_vector]
for j in range(20):
    x2.append(x2[j] + x_vector)
    
x3 = [x1[0] + y_vector]
for k in range(21):
    x3.append(x3[k] + x_vector)
x4 = [x3[0] + z_vector]
for l in range(20):
    x4.append(x4[l] + x_vector)

x5 = [x3[0] + y_vector]
for m in range(21):
    x5.append(x5[m] + x_vector)
    
x6 = [x5[0] + z_vector]
for l in range(20):
    x6.append(x6[l] + x_vector)

x7 = [x5[0] + y_vector]
for m in range(21):
    x7.append(x7[m] + x_vector)
    
x8 = [x7[0] + z_vector]
for l in range(20):
    x8.append(x8[l] + x_vector)
    
x9 = [x7[0] + y_vector]
for m in range(21):
    x9.append(x9[m] + x_vector)
    
x10 = [x9[0] + z_vector]
for l in range(20):
    x10.append(x10[l] + x_vector)

x11 = [x9[0] + y_vector]
for m in range(21):
    x11.append(x11[m] + x_vector)
    
x12 = [x11[0] + z_vector]
for l in range(20):
    x12.append(x12[l] + x_vector)
    
x13 = [x11[0] + y_vector]
for m in range(21):
    x13.append(x13[m] + x_vector)
    
x14 = [x13[0] + z_vector]
for l in range(20):
    x14.append(x14[l] + x_vector)
    

x15 = [x13[0] + y_vector]
for m in range(21):
    x15.append(x15[m] + x_vector)
    
x16 = [x15[0] + z_vector]
for l in range(20):
    x16.append(x16[l] + x_vector)
    
x17 = [x15[0] + y_vector]
for m in range(21):
    x17.append(x17[m] + x_vector)
    
x18 = [x17[0] + z_vector]
for l in range(20):
    x18.append(x18[l] + x_vector)
    
x19 = [x17[0] + y_vector]
for m in range(21):
    x19.append(x19[m] + x_vector)
    
x20 = [x19[0] + z_vector]
for l in range(20):
    x20.append(x20[l] + x_vector)
    
x21 = [x19[0] + y_vector]
for m in range(21):
    x21.append(x21[m] + x_vector)
    
x22 = [x21[0] + z_vector]
for l in range(20):
    x22.append(x22[l] + x_vector)
    
x23 = [x21[0] + y_vector]
for m in range(21):
    x23.append(x23[m] + x_vector)
    
x24 = [x23[0] + z_vector]
for l in range(20):
    x24.append(x24[l] + x_vector)
    
x25 = [x23[0] + y_vector]
for m in range(21):
    x25.append(x25[m] + x_vector)
    
x26 = [x25[0] + z_vector]
for l in range(20):
    x26.append(x26[l] + x_vector)
    
x27 = [x25[0] + y_vector]
for m in range(21):
    x27.append(x27[m] + x_vector)
    
x28 = [x27[0] + z_vector]
for l in range(20):
    x28.append(x28[l] + x_vector)
    
    
x29 = [x27[0] + y_vector]
for m in range(21):
    x29.append(x29[m] + x_vector)
    
x30 = [x29[0] + z_vector]
for l in range(20):
    x30.append(x30[l] + x_vector)
    
    
    
x31 = [x29[0] + y_vector]
for m in range(21):
    x31.append(x31[m] + x_vector)
    
x32 = [x31[0] + z_vector]
for l in range(20):
    x32.append(x32[l] + x_vector)
    
x33 = [x31[0] + y_vector]
for m in range(21):
    x33.append(x33[m] + x_vector)
    
x34 = [x33[0] + z_vector]
for l in range(20):
    x34.append(x34[l] + x_vector)
    

x35 = [x33[0] + y_vector]
for m in range(21):
    x35.append(x35[m] + x_vector)
    
x36 = [x35[0] + z_vector]
for l in range(20):
    x36.append(x36[l] + x_vector)
    
x37 = [x35[0] + y_vector]
for m in range(21):
    x37.append(x37[m] + x_vector)
    
x38 = [x37[0] + z_vector]
for l in range(20):
    x38.append(x38[l] + x_vector)
    
x39 = [x37[0] + y_vector]
for m in range(21):
    x39.append(x39[m] + x_vector)
    
x40 = [x39[0] + z_vector]
for l in range(20):
    x40.append(x40[l] + x_vector)
    
x41 = [x39[0] + y_vector]
for m in range(21):
    x41.append(x41[m] + x_vector)
    
x42 = [x41[0] + z_vector]
for l in range(20):
    x42.append(x42[l] + x_vector)
    
x43 = [x41[0] + y_vector]
for m in range(21):
    x43.append(x43[m] + x_vector)
    
x44 = [x43[0] + z_vector]
for l in range(20):
    x44.append(x44[l] + x_vector)
    
x45 = [x43[0] + y_vector]
for m in range(21):
    x45.append(x45[m] + x_vector)
    
x46 = [x45[0] + z_vector]
for l in range(20):
    x46.append(x46[l] + x_vector)
    
x47 = [x45[0] + y_vector]
for m in range(21):
    x47.append(x47[m] + x_vector)
    
x48 = [x47[0] + z_vector]
for l in range(20):
    x48.append(x48[l] + x_vector)
    
x49 = [x47[0] + y_vector]
for m in range(21):
    x49.append(x49[m] + x_vector)
    
x50 = [x49[0] + z_vector]
for l in range(20):
    x50.append(x50[l] + x_vector)
    
x51 = [x49[0] + y_vector]
for m in range(21):
    x51.append(x51[m] + x_vector)
    
x52 = [x51[0] + z_vector]
for l in range(20):
    x52.append(x52[l] + x_vector)
    
x53 = [x51[0] + y_vector]
for m in range(21):
    x53.append(x53[m] + x_vector)
    
x54 = [x53[0] + z_vector]
for l in range(20):
    x54.append(x54[l] + x_vector)
    
x55 = [x53[0] + y_vector]
for m in range(21):
    x55.append(x55[m] + x_vector)
    
x56 = [x55[0] + z_vector]
for l in range(20):
    x56.append(x56[l] + x_vector)




obs = np.unique(np.array(x1 + x2 + x3 + x4 + x5 +x6 + x7 + x8 +x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 +x19 + x20 + x21 + x22 +x23 + x24 +x25 + x26 +x27 + x28 +x29 + x30 + x31 + x32 +x33 + x34 +x35 + x36 + x37 + x38 + x39 + x40 + x41 +x42 + x43 + x44 + x45 + x46 + x47 + x48 ), axis = 0)

plt.figure(figsize=(10,8))
plt.plot(obs[:,0], obs[:,1], marker = 'o', linestyle = '')
plt.show()
np.savetxt('data.xyz', obs, delimiter = '\t')