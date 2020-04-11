# -*- coding: utf-8 -*-

'''
Created on 2020/04/10

@author: https://qiita.com/goodboy_max
'''

###########################################################################################
#
# 世界的に関心の高い新型コロナウイルスの感染状況を
# ジョンズホプキンス大学がGitHub↓に公開しているCSVデータを辞書形式として集計する。
#
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
#
# CSVヘッダの内容を確認し名寄せ処理を行う。
# 対象となる国を指定して日付別の辞書型データとして永続化する。
#
# 【前提】
# ローカルにCSVファイルが取得されていること。
#
#
###########################################################################################

# 必要モジュールのインポート
import csv
import os.path
import pickle

from dateutil.parser import parse

#from tinydb import TinyDB, Query

dir_path = "csse_covid_19_data/csse_covid_19_daily_reports"
dic_path = "csse_covid_19_data/covid_19_daily_reports_dic.pickle"

files = []

Country_Region = "Japan"

Country_key = '国名'
Confirmed_key  = '感染者数'
Death_key = '死者数'
Recovered_key = '退院者数'

# CSVファイル順に配列へ格納する
date = []
countory = []
confirmed  = []
death = []
recovere = []

#################################################################
# pickleでリストや辞書を外部ファイルに保存
#################################################################
def pickle_dump(obj, path):
    with open(path, mode='wb') as f:
        pickle.dump(obj,f)

#################################################################
# pickleでリストや辞書を外部ファイルから読み込み
#################################################################
def pickle_load(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
        return data

#################################################################
# 指定したディレクトリのファイルを取得する
#################################################################
def get_file(dir_path):

#    pre_header = ""

    for filename in os.listdir(dir_path):
        content_full_path = os.path.join(dir_path, filename)

        if content_full_path[-4:] == ".csv":
            print (content_full_path)

            with open(content_full_path, 'r', encoding='utf-8-sig') as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:

                    # header_1 = ["Province/State", "Country/Region", "Last Update", "Confirmed", "Deaths", "Recovered"]
                    # header_2 = ["FIPS","Admin2","Province_State","Country_Region","Last_Update,Lat","Long_","Confirmed","Deaths","Recovered","Active","Combined_Key"]
                    #
                    #CSVのヘッダ項目と項目数や項目の位置がファイルによって異なるので項目名でデータを収集する。

                    if row.get('Country/Region') == Country_Region:

#                        print ("Country/Region Japan ｷﾀ―――(ﾟ∀ﾟ)―――― !!")

                        # 日付フォーマット変換
                        dt = parse(row.get('Last Update'))
                        tdate = f'{dt: %Y-%m-%d}'
                        date.append(tdate)

                        countory.append(row.get('Country/Region'))

                        confirmed.append(row.get('Confirmed'))
                        death.append(row.get('Deaths'))
                        recovere.append(row.get('Recovered'))

                    elif row.get('Country_Region') == Country_Region :

#                        print ("Country_Region Japan ｷﾀ―――(ﾟ∀ﾟ)―――― !!")

                        # 日付フォーマット変換
                        dt = parse(row.get('Last_Update'))
                        tdate = f'{dt: %Y-%m-%d}'
                        date.append(tdate)

                        countory.append(row.get('Country_Region'))

                        confirmed.append(row.get('Confirmed'))
                        death.append(row.get('Deaths'))
                        recovere.append(row.get('Recovered'))

    return("CSV読み込み完了 ｷﾀ―――(ﾟ∀ﾟ)―――― !!")

def main():
    #################################################################
    # CSVファイルの読み出し
    #################################################################
    result = get_file(dir_path)
    print(result)

    #################################################################
    # zip関数を使って複数要素を１つにして日付別の辞書型にまとめる。
    #################################################################
    dic = {date_key : {Country_key : value1, Confirmed_key : value2, Death_key : value3, Recovered_key : value4}
        for date_key,value1,value2,value3,value4
        in zip(date, countory,confirmed ,death,recovere)}

    print(dic)

    #################################################################
    # 辞書型データの永続化
    #################################################################
    pickle_dump(dic, dic_path)

    #################################################################
    # 永続化した辞書型ファイルを取り出す
    #################################################################
    print(pickle_load(dic_path))

    print ("辞書型データの確認 ｷﾀ―――(ﾟ∀ﾟ)―――― !!")

if __name__ == "__main__":
    main()
