# AtCoder-AC-prog
## 概要
[togatoga](https://github.com/togatoga)様の[procon-gardener](https://github.com/togatoga/procon-gardener)を実行し、Pushするという一連の動作を自動化したものです。

## 使用方法
### 1. `main.py`の変数`path`にPushしたいローカルリポジトリへのパスを記入
```
path = ''
```
### 2. コマンドを入力し、プログラムを実行
```
> python main.py
```
### 3. `procon-gardener archive`コマンドを実行し、ACしたコードが取得する
もし、ACしたコードがない場合はこの時点で終了する
### 4. 取得したコードをリモートリポジトリへPush
Pushが終われば、プログラムの実行は終了する

## 活用方法
タスクスケジューラなどで定期的に自動実行させれば、ACしたコードが自動的にPushされる仕組みが作れると思います


