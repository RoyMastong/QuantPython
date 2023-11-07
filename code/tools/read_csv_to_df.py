# -*- coding = utf-8 -*-

# @time:2023/11/7 15:37
# @Author:Junqi Chen
# @File:read_csv_to_df.py
# @Software:PyCharm


import pandas as pd
import numpy as np
import datatable as dt
from datetime import datetime
import stat_time

path = '/Users/chenjunqi/Downloads/vi_2023_origin.csv'


@stat_time.calculate_execution_time
def usePandsReadCsv(path):

    # read csv file to pandas dataframe
    df = pd.read_csv(path)

    # look at the first 5 rows of the dataframe
    print(df.head())


@stat_time.calculate_execution_time
def useDataTableReadCsv(path):

    # read csv file to datatable
    df = dt.fread(path)

    # trans datatable to pandas dataframe
    # df = df.to_pandas()
    print(df.head())
    return df


if __name__ == '__main__':
    usePandsReadCsv(path)
    # useDataTableReadCsv(path)