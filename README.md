# WatsonAssistant-Funtions-Sample
Qiita記事「[情報提供型のチャットボット(Watson Assistant/Functions/Db2連携)で複数件の結果を扱う方法]()」のサンプルです

## セットアップ手順
### 1. サービス・インスタンスの作成
- Watson Assistant
- Db2
### 2. Db2テーブルの作成
- Db2のコンソールを使ってテーブル **ACTION_MOVIE**を作りData.csvをロードします
### 3. Functionsの作成
- function/SELECT_MOVIES.pyのDb2接続文字列・スキーマ、テーブル名を変更します
- FunctionsのUIまたはCLIにてSELECT_MOVIESを定義します
　( Cliならibmcloud fn action create SELECT_MOVIES SELECT_MOVIES.py --kind python:3.7 )
 
### 4. Assistant環境の作成
- assistant/skill-ActionMovie.jsonをインポートします
- Function起動文字列の

```
