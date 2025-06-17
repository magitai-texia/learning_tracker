# 📘 学習 記録 アプリ

学習時間を記録し、進捗を可視化するシンプルなアプリケーションです。

Python をバックエンドに、HTML/CSS/JavaScript をフロントエンドに使用し、Chart.js を活用して学習データをグラフで表示します。

---

## 🚀 特長

- **学習時間の記録**：日々の学習時間を簡単に入力・保存
- **進捗の可視化**：Chart.js を使用して、学習時間の推移をグラフで表示
- **シンプルな UI**：直感的なインターフェースで、誰でもすぐに使い始められる

---

## 🛠 使用技術

- **バックエンド**：Python（Flask）
- **フロントエンド**：HTML, CSS, JavaScript
- **グラフ描画**：Chart.js（CDN 経由で読み込み）
- **データ保存**：JSON ファイル（`data.json`）

---

## 📦 インストールと起動方法

### 1. 必要なソフトウェアのインストール

- Python 3.8 以上がインストールされていることを確認してください。

### 2. リポジトリのクローン

```bash
git clone https://github.com/magitai-texia/learning_tracker.git
cd learning_tracker
```

### 3. 仮想環境の作成と依存関係のインストール

```bash
python -m venv venv
venv\Scripts\activate  # Windows の場合
source venv/bin/activate  # macOS/Linux の場合
pip install -r requirements.txt
```

### 4. アプリケーションの起動

```bash
python app.py
```

ブラウザで http://127.0.0.1:5000 にアクセスすると、アプリケーションが表示されます。

### 📄 ファイル構成

```pgsql
learning_tracker/
├── app.py
├── data.json
├── requirements.txt
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    └── index.html
```

### 📝 ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。詳細は LICENSE ファイルをご覧ください。

### 💬 貢献
バグ報告や機能追加の提案は、Issues を通じてお知らせください。プルリクエストも歓迎します！

