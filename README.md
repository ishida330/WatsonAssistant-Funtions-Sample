# WatsonAssistant-Funtions-Sample
Qiita記事「[情報提供型のチャットボット(Watson Assistant/Functions/Db2連携)で複数件の結果を扱う方法]()」のサンプルです

## セットアップ手順
### 1. サービス・インスタンスの作成
- Watson Assistant
- Db2
### 2. Db2テーブルの作成
- Db2のコンソールを使ってテーブル **ACTION_MOVIE**を作りACTION_MOVIE.csvをロードします
  ![Db2load](https://user-images.githubusercontent.com/9675895/63083390-93a20280-bf83-11e9-9f7d-a216e55d057c.png)

- Functionのロジックに記入するために以下を記録します
  -接続文字列: Db2-サービス資格情報-dsn
   例) "dsn": "DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxxxxxxx;PWD=xxxxxxxx;",
   -スキーマとテーブル名
   

### 3. Functionsの作成
- function/SELECT_MOVIES.pyのDb2接続文字列・スキーマ、テーブル名を変更します
- FunctionsのUIまたはCLIにてSELECT_MOVIESを定義します
　( Cliならibmcloud fn action create SELECT_MOVIES SELECT_MOVIES.py --kind python:3.7 )
 
### 4. Assistant環境の作成
- assistant/skill-ActionMovie.jsonをインポートします
  ![import_skill](https://user-images.githubusercontent.com/9675895/63082531-694f4580-bf81-11e9-8cbf-efab64e1a1aa.png)

- Function起動文字列の<<change me!>>欄3つをご自身の環境に合わせて変更します
  - name: Functions-Actions-SELECT_MOVIES-エンドポイント-REST API-URLの /namespacesの後ろ
          例) https://us-south.functions.cloud.ibm.com/api/v1/namespaces/ibmho023%40yahoo.co.jp_dev/actions/SELECT_MOVIES
  
  - user/password: Functions->この名前空間の設定->この名前空間の CF ベースの API 鍵
          例) **user**:**password**
 
 　![change_function_def](https://user-images.githubusercontent.com/9675895/63082590-956ac680-bf81-11e9-9cc4-5a79844ac11d.png)

- Try it outで稼働確認
    ![TryItOut](https://user-images.githubusercontent.com/9675895/63082604-9bf93e00-bf81-11e9-96bc-71f346f548cc.png)
