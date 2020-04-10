# covid19

## PyGithubを使って、GitHub上のファイルを取得するサンプル。

世界的に関心の高い新型コロナウイルスの感染状況を
ジョンズホプキンス大学がGitHub↓に公開しているので

https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

から日々のデータを取得し、データを操作する。

## 前提
- python3環境が構築済であること。

- 開発環境構築時に以下のコマンドで利用モジュールの取得が必要

 pip install PyGithub

- Githubにアカウントを持っていて個人用アクセスtorken を取得しておくこと

 取得方法は下記参照

 https://help.github.com/ja/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

 セキュリティ上の理由から、 GitHub は過去 1 年間使用されていない個人アクセストークンを自動的に削除するので注意が必要。
