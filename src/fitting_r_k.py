import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

file_path_th = '.\data_processing\ex\*through_E*.csv'
file_path_cr = '.\data_processing\ex\*cross_E*.csv'
csv_1 = []
csv_2 = []
x_axis = []
th_sum = []
cr_sum = []

# through


for filename_1 in glob.glob(file_path_th, recursive=True):
    csv_1.append(filename_1)

    for file_1 in csv_1:
        filename_1 = file_1.split('\\')[-1][:-4]
        data_1 = pd.read_csv('.\data_processing\ex\%s.csv'%filename_1, names=['first'])
        final_sum_1 = 0
        integer_1 = list(range(0,list(data_1.shape)[0]))
        data_1.index = integer_1
        data_1.index.name = 'order'
    for i in range(0,list(data_1.shape)[0]):
        find_value_1 = data_1['first'][i]
        find_value_1 = find_value_1.split()
        key_1 = list(map(float, find_value_1))
        sum_1 = 0
        for x in range(0,len(key_1)):
            sum_1 +=float(key_1[x])
        #print('%d번째 합 = '%i,sum_1)
        final_sum_1 = sum_1 + final_sum_1
    #x_axis.append(int(filename_1[-3:]))
    th_sum.append(final_sum_1)
    #print('%s의 값 ='%filename,final_sum)
#print(x_axis)
#print(th_sum)

# cross

for filename_2 in glob.glob(file_path_cr, recursive=True):
    csv_2.append(filename_2)

    for file_2 in csv_2:
        filename_2 = file_2.split('\\')[-1][:-4]
        data_2 = pd.read_csv('.\data_processing\ex\%s.csv'%filename_2,names=['first'])
        final_sum_2 = 0
        integer_2 = list(range(0,list(data_2.shape)[0]))
        data_2.index = integer_2
        data_2.index.name = 'order'
    for i in range(1,list(data_2.shape)[0]):
        find_value_2 = data_2['first'][i]
        find_value_2 = find_value_2.split()
        key_2 = list(map(float, find_value_2))
        #print(find_value_2)
        sum_2 = 0
        for x in range(0,len(key_2)):
            sum_2 +=float(key_2[x])
        #print('%d번째 합 = '%i,sum_2)
        final_sum_2 = sum_2 + final_sum_2
    cr_sum.append(final_sum_2)
    #print('%s의 값 ='%filename_2,final_sum_2)
#print(cr_sum)

# calculation
th_sum_square_list = []
cr_sum_square_list = []
th_cr_sum_list = []
r_value_list = []
k_value_list = []

for j in range(0,len(th_sum)):
    th_sum_square = th_sum[j]*th_sum[j]
    cr_sum_square = cr_sum[j]*cr_sum[j]
    th_sum_square_list.append(th_sum_square)
    cr_sum_square_list.append(cr_sum_square)
    th_cr_sum = th_sum_square + cr_sum_square
    th_cr_sum_list.append(th_cr_sum)
    r_value = np.sqrt(th_sum_square / th_cr_sum)
    k_value = np.sqrt(cr_sum_square / th_cr_sum)
    r_value_list.append(r_value)
    k_value_list.append(k_value)


def run(x, y, z):
    plt.scatter(x, y)
    plt.scatter(x, z)
    plt.plot(x,y)
    plt.plot(x,z)
    plt.title('Power by r,k')
    plt.xlabel('distance [nm]',labelpad=10)
    plt.ylabel('Power [W]',labelpad=10)
    plt.legend()
    plt.grid(True)
    plt.show()

