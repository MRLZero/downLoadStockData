# coding=utf-8
from getJPHistoryData import getJPHistoryData
from utils import *

if __name__ == '__main__':

    codes = ['7203']
    save_path = 'data/fundsHistoryValue'
    for code in codes:
        df = getJPHistoryData(code)
        saveFundHistoryValues(code, df, save_path)