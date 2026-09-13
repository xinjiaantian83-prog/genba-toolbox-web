# 現場電卓 SEOサイト

外構・土木・建設の現場計算を検索するユーザーに、計算方法と無料アプリ「現場電卓」を案内する静的サイトです。

## 更新

```bash
python3 scripts/build.py
```

GitHub Pagesは `main` ブランチ直下を公開元として設定します。

## 現場電卓 Web版（未公開）

アプリ版の主要機能をブラウザで使える試作版は `web/` に生成します。

```bash
python3 scripts/build_web_app.py
python3 -m http.server 4174
```

確認URL: `http://127.0.0.1:4174/web/`
