import matplotlib.pyplot as plt

pop_ages = [22,55,62,45,21,22,34,24,44,4,99,102,110,12,100,24,70,50,43,55,28,29,23,30,80,8]

#ids= [x for x in range(len(pop_ages))]]

bins =[0,10,20,30,40,50,60,70,80,90,100,120,130]


plt.hist(pop_ages,bins, histtype='bar',rwidth=0.8)


plt.xlabel('x')
plt.ylabel('y')
plt.title('First Graph\n sub-title')
plt.legend()
plt.show()
