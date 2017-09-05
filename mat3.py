import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 =[1,3,5,9,11]
y2 =[8,7,2,4,2]

plt.bar(x,y, label='bars1',color='red')
plt.bar(x2,y2, label='bars2', color='blue')


plt.xlabel('x')
plt.ylabel('y')
plt.title('First Graph\n sub-title')
plt.legend()
plt.show()
