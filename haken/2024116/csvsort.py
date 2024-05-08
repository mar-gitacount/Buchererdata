import pandas as pd

# CSVファイルのパス
csv_file_path = 'output.csv'

# 列の番号（0-indexed）
column_number = 2  # 例として3列目を指定

# CSVファイルを2行目から読み込み
df = pd.read_csv(csv_file_path, header=1)

# 指定した列を基準に行をソート
df_sorted = df.sort_values(by=df.columns[column_number])

# ソート後のデータを新しいCSVファイルに保存
new_csv_file_path = 'file_sorted.csv'
df_sorted.to_csv(new_csv_file_path, index=False)
