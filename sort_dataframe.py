import pandas as pd
from pathlib import Path

# 1. 実行環境（スクリプトかJupyterか）に合わせてパスを安全に取得
try:
    base = Path(__file__).parent.parent
except NameError:
    base = Path.cwd()  # Jupyterなどの場合は現在の作業ディレクトリを基準にする

input_file = base / "data" / "sales1.csv"
output_folder = base / "output"
output_folder.mkdir(parents=True, exist_ok=True)

# 2. ファイルの存在チェック
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"エラー: ファイルが見つかりません → {input_file}")
    print("フォルダの構成やファイル名を確認してください。")
    exit()

print("列:", list(df.columns))

# 3. 列名の入力と存在チェック
col = input("並び替える列名: ").strip()
if col not in df.columns:
    print(f"エラー: '{col}' という列は存在しません。上の列名リストから選んでください。")
    exit()

order = input("降順なら d、昇順なら a を入力: ").strip()
ascending = order.lower() != "d"

# 4. 並び替えと保存
try:
    sorted_df = df.sort_values(by=col, ascending=ascending)
    output_path = output_folder / "並び替え結果.xlsx"
    sorted_df.to_excel(output_path, index=False)
    print(f"完了: {output_path}")
except Exception as e:
    print(f"エラーが発生しました: {e}")