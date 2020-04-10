# -*- coding: utf-8 -*-

'''
Created on 2020/04/07

@author: https://qiita.com/goodboy_max
'''

###########################################################################################
#
# PyGithubを使って、GitHub上のファイルを取得するサンプル。
#
# 世界的に関心の高い新型コロナウイルスの感染状況を
# ジョンズホプキンス大学がGitHub↓に公開しているので、
#
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# から日々のデータを取得してみる。
#
# なお既に存在するファイルの場合は取得しない。
# 取得してわかったけどヘッダ情報も集計データも途中で変わっちゃうんだよね。
# この後のデータ項目の丸め処理がめんどくさそう・・・
#
# 【前提】
# 開発環境構築時に以下のコマンドで利用モジュールの取得が必要。
# pip install PyGithub
#
# また、Githubにアカウントを持っていて個人用アクセスtorken を取得しておくことも必要。
# 取得方法は下記参照
#
# https://help.github.com/ja/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
#
# セキュリティ上の理由から、 GitHub は過去 1 年間使用されていない個人アクセストークンを
# 自動的に削除するので注意が必要。
#
###########################################################################################

# 必要モジュールのインポート
import os.path
import base64
from github import Github

token = "******your_token******"
# https://help.github.com/ja/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

repository = "CSSEGISandData/COVID-19"
dir_path = "csse_covid_19_data/csse_covid_19_daily_reports"

#################################################################
# 指定したディレクトリのファイルを取得
#################################################################
def get_file(dir_path):

    g = Github(token)

    repo = g.get_repo(repository)

    contents = repo.get_contents(dir_path)

    #コンテンツがなくなるまで処理
    while contents:
        file_content = contents.pop(0)

        # 指定したディレクトリの下にディレクトリが無いか念のため確認
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
            print(file_content.path)

        else:
            # 最後の4文字が .csv のファイルのみ取得
            if file_content.path[-4:] == ".csv":

                # ローカルにファイルが存在しない場合のみ追加
                if os.path.exists(file_content.path) == False:
                    print ("ファイル追加 ： " + file_content.path)
                    file_contents = repo.get_contents(file_content.path)

                    # コンテンツの中身はBase64でデコードする。
                    # https://developer.github.com/v3/repos/contents/
                    content = base64.b64decode(file_contents.content)

                    # ローカルのファイルを追加
                    with open(file_content.path, mode="wb") as f:
                        f.write(content)

    return("ｷﾀ―――(ﾟ∀ﾟ)―――― !!")

def main():
        result = get_file(dir_path)
        print(result)

if __name__ == "__main__":
    main()
