# csgの欲しいものリストを管理するwebアプリケーション

## 仕様(予定)

ユーザ情報を登録し、だれがその商品を入れたのかを可視化する。また、誰かがほしいものリストに商品を入れた際にその情報をslackにて通知する。

Djangoで作成予定。

開発ブランチはdev。新規機能を追加する場合はブランチを分けること。

## 進捗

* ~~ユーザ登録画面(5/7現在　実装済み)~~
* ~~商品の登録と管理(5/4実装済み)~~
* slackの通知
* 商品のサムネイル
* ユーザの管理
    * 欲しいものリストの商品に対してrootと登録したユーザ以外がアクセスすることを制限するようにすること。