import hashlib
import csv

def generate_hash(row):
    # type,question,answerを結合してMD5ハッシュ生成
    data = f"{row['type']},{row['question']},{row['answer']}"
    return hashlib.md5(data.encode('utf-8')).hexdigest()

# 入力/出力ファイル
input_file = 'words.csv'
output_file = 'database.csv'

# words.csv読み込み
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, fieldnames=['type', 'question', 'answer'])
    rows = list(reader)

# ハッシュ生成＋database.csv書き込み
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['hash', 'type', 'question', 'answer'])  # ヘッダー
    for row in rows:
        hash_value = generate_hash(row)
        writer.writerow([hash_value, row['type'], row['question'], row['answer']])

print(f"Generated {output_file} with {len(rows)} rows.")
