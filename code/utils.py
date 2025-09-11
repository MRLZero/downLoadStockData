# coding=utf-8
import os
import time

def mkdir(path):
    path = path.strip()
    path = path.rstrip('/')
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print("Create {} OK!".format(path))
        return True
    else:
        print("Path: {} already exists!".format(path))
        return False

def saveFundHistoryValues(code, historyValues, historyValuesSavePath):
    nowdate = time.strftime('%Y-%m-%d', time.localtime())
    historyValuesSavePath = os.path.join(historyValuesSavePath, nowdate)
    mkdir(historyValuesSavePath)
    file = '{}_history_data.csv'.format(code)
    file = os.path.join(historyValuesSavePath, file)
    new_df = historyValues[['净值日期', '累计净值']]
    new_df.to_csv(file, index=False, encoding='gbk')
    print("save {} ok!\n".format(file))