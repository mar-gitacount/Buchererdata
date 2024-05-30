# sqlite_data_insert.py

import sqlite3

class SQLiteDataInsert:
    def __init__(self, db_file,table_name,fields):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        # テーブル名
        self.table_name = table_name
        # フィールド名
        self.fields = fields
    

         
    # フィールドのなかの値の数を返す。
    def fieldcountAllcountcheck(self,):
         print(self.table_name,"テーブル名をチェックする")
        # self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        #  self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
         self.cursor.execute(f"SELECT MAX({self.fields[0]}) FROM {self.table_name}")
      
        # プライマリキーは一番目と想定して実装している。
         count = self.cursor.fetchall()[0][0]
         testcount = count + 1
         print(f"{count}はもともとのカウント→は1足したやつ{testcount}")
         count += 1

         
         return count
        #  print(query)
    
    # データを確認。
    def datacountcheck(self, value, field):
         query = f"SELECT COUNT(*) FROM {self.table_name} WHERE {field} = ?"
        #  query = f"SELECT MAX({primary_key_field}) FROM {self.table_name}"
         self.cursor.execute(query, (value,))
         count = self.cursor.fetchone()[0]
         return count > 0

    
    def insert_data(self,values):
         # 動的なプレースホルダーのリスト
        
            placeholders = ', '.join(['?'] * (len(self.fields)))
            print(self.table_name)
            print(placeholders)
            # 一番目にfieldcountを入れ込む
            incrementnum = self.fieldcountAllcountcheck()
            values.insert(0,incrementnum)

            print(self.fields,"←値確認この数も合わせなければならない")
            print(values)
            print("ここでエラーになる")
            # 動的なフィールドのリストを文字列に変換
            fields_str = ', '.join(self.fields)
            # ここでクエリを検索して存在確認し、それのidを取得してincrementnumを上書きする。
            # 動的なクエリを生成
            query = f"INSERT OR REPLACE INTO {self.table_name} ({fields_str}) VALUES ({placeholders})"
            self.cursor.execute(query, values)
            self.conn.commit()  # トランザクションをコミット

    
    def insert_watch_item(self, table_name,bucherer_watch_id, year, model_name, ref, bracelet, dial, url):
        try:
            # self.cursor.execute('''INSERT INTO {}(bucherer_watch_id, year, model_name, ref, bracelet, dial, url) VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(table_name),
            #(bucherer_watch_id, year, model_name, ref, bracelet, dial, url))
            query = '''INSERT OR REPLACE INTO {} (bucherer_watch_id, year, model_name, ref, bracelet, dial, url) VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(table_name)
            self.cursor.execute(query, (bucherer_watch_id, year, model_name, ref, bracelet, dial, url))
            self.conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print("Error occurred while inserting data:", e)
    
    # 渡された日付 + 4日分を検索する。日付は呼び出し元で設定する配列を返すメソッドにする予定。
    def weeksitemdiffcheck(self,days):
        #  日付n日分を全て検索そのアイテムをn+1,n+2....に存在するか確認存在した場合、配列のn+k番目に代入する。→独自のテーブルを作る？n+kで独自のテーブルを検索して存在した場合、true
         for day in days:
              print(day)
            #   日付nのアイテムループする。
         return

    def close_connection(self):
        self.conn.close()
