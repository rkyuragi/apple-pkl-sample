# apple-pkl-sample

[公式ドキュメント](https://pkl-lang.org/main/current/index.html)

## pklインストール

```shell
curl -L -o pkl https://github.com/apple/pkl/releases/download/0.25.2/pkl-macos-aarch64
chmod +x pkl
./pkl --version
```

### pkl options

```shell
  eval              Render pkl module(s)
  repl              Start a REPL session
  server            Run as a server that communicates over standard
                    input/output
  test              Run tests within the given module(s)
  project           Run commands related to projects
  download-package  Download package(s)
```

## VSCode拡張機能

https://github.com/apple/pkl-vscode/releases

vsixファイルをvscodeに追加


## サンプル

serverless frameworkのyamlファイルをpklに変換してみたコード

*参考にしたyamlファイル:[here](https://dev.classmethod.jp/articles/serverless-yml-read-external-file/)*

`./sample/serverlessframework/serverless.yaml`

### 実行

#### yamlファイルの作成

```shell
./pkl eval -f yaml sample/serverlessframework/serverless.pkl -o sample/serverlessframework/serverless-output.yaml
```

#### Pklから作成したyamlと元になったyamlを比較して問題ないことを確認

```shell
pipenv run python diffyaml.py
```
