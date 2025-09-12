# coding=utf-8
from getJPHistoryData import getJPHistoryData
from utils import *

if __name__ == '__main__':

    codes = ['1332', '1605', '1721', '1801', '1802', '1803', '1808', '1812', '1925', '1928', '1963', '2002', '2269'
             ]

    save_path = 'data/fundsHistoryValue'
    for code in codes:
        df = getJPHistoryData(code)
        df = process_qfq_value(df)
        saveFundHistoryValues(code, df, save_path)