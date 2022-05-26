import pandas as pd
import numpy as np
import glob
import shutil
import os.path
import os
import sys

sys.path.append("../run_graph.py")



#file_list = os.listdir('../data_processing')
txt_to_csv = './data_processing/ex/*.txt'

#run.name_list = ['50', '150', '250', '350', '450', '550']
csv_1 = []

def txt_drop(x, name):
    if x == 0:
        for i in range(0, len(name)):
            with open('./data_processing/ex/cross_E_{}nm.txt'.format(name[i]),'r') as fin:
                data = fin.read().splitlines(True)
            with open('./data_processing/ex/cross_E_{}nm.txt'.format(name[i]), 'w') as fout:
                fout.writelines(data[1:])
            with open('./data_processing/ex/through_E_{}nm.txt'.format(name[i]),'r') as fin:
                data = fin.read().splitlines(True)
            with open('./data_processing/ex/through_E_{}nm.txt'.format(name[i]), 'w') as fout:
                fout.writelines(data[1:])
    else:
        print('complete converting')


def convert(y):
    if y == 0:
        files = glob.glob(txt_to_csv)
        for i in files:
            if not os.path.isdir(i):
                filename = os.path.splitext(i)
                try:
                    os.rename(i,filename[0] + '.csv')
                except:
                    pass
    else:
        print('no')

'''
'''
'''
f = ''
text = []
for k in range(0, len(file_list)):
    print(file_list[k])
    print(file_list[0][:-4])


    for filename in glob.glob(file_list[k], recursive=True):
        text.append(filename)
        print(text)
        for file_1 in text:
            filename_1 = file_1.split('\\')[-1][:-4]
            data_1 = pd.read_csv('.\data_processing\%s.text'%filename_1)
'''
'''
th_50 = pd.read_csv('./data_processing/through_E_50nm.txt')
th_150 = pd.read_csv('./data_processing/through_E_150nm.txt')
th_250 = pd.read_csv('./data_processing/through_E_250nm.txt')
th_350 = pd.read_csv('./data_processing/through_E_350nm.txt')
th_450 = pd.read_csv('./data_processing/through_E_450nm.txt')
th_550 = pd.read_csv('./data_processing/through_E_550nm.txt')

th_50_c = th_50.to_csv('./data_processing/through_E_050.csv')
th_150_c = th_150.to_csv('./data_processing/through_E_150.csv')
th_250_c = th_250.to_csv('./data_processing/through_E_250.csv')
th_350_c = th_350.to_csv('./data_processing/through_E_350.csv')
th_450_c = th_450.to_csv('./data_processing/through_E_450.csv')
th_550_c = th_550.to_csv('./data_processing/through_E_550.csv')

cr_50 = pd.read_csv('./data_processing/cross_E_50nm.txt')
cr_150 = pd.read_csv('./data_processing/cross_E_150nm.txt')
cr_250 = pd.read_csv('./data_processing/cross_E_250nm.txt')
cr_350 = pd.read_csv('./data_processing/cross_E_350nm.txt')
cr_450 = pd.read_csv('./data_processing/cross_E_450nm.txt')
cr_550 = pd.read_csv('./data_processing/cross_E_550nm.txt')

cr_50_c = cr_50.to_csv('./data_processing/cross_E_050.csv')
cr_150_c = cr_150.to_csv('./data_processing/cross_E_150.csv')
cr_250_c = cr_250.to_csv('./data_processing/cross_E_250.csv')
cr_350_c = cr_350.to_csv('./data_processing/cross_E_350.csv')
cr_450_c = cr_450.to_csv('./data_processing/cross_E_450.csv')
cr_550_c = cr_550.to_csv('./data_processing/cross_E_550.csv')
'''
'''
cr_50 = pd.read_csv('./data_processing/cross_E_050.csv', names=['first', 'second'])
integer = list(range(0, list(cr_50.shape)[0]))
cr_50.index = integer
cr_50.index.name = 'order'
for i in range(0, list(cr_50.shape)[0]):
    find_value = cr_50.loc[i].second
    find_value = find_value.split()
    key = list(map(float, find_value))
    sum = 0
    for x in range(0, len(key)):
        sum += float(key[x])
    print('%d번째 합 = ' % i, sum)
'''