# coding=utf-8
import yfinance as yf
from utils import *

def getJPHistoryData(code):
    # 获取日本数据（'.T'对应日本）
    code = str(code).strip() + '.T'
    end = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    df = yf.download(code, start="2000-01-01", end=end, auto_adjust=True, multi_level_index=False)
    df.reset_index(inplace=True)
    new_df = df[['Date', 'Close']]
    new_df.columns = ['净值日期', '累计净值']
    return new_df

if __name__ == '__main__':

    codes = ['7203']
    save_path = 'data/fundsHistoryValue'
    for code in codes:
        df = getJPHistoryData(code)
        df = process_qfq_value(df)
        saveFundHistoryValues(code, df, save_path)


