import tkinter as tk
import psycopg2
from psycopg2 import Error
from tkinter import ttk

# 建立與資料庫的連接
host = "****"
dbname = "****"
user = "****"
password = "****"
sslmode = "****"

def connect_to_database():
    try:
        conn = psycopg2.connect(host=host, port=5432, user=user, password=password, database=dbname, sslmode=sslmode)
        conn.cursor().execute("SET timezone = 'Asia/Hong_Kong'")
        return conn
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

# 執行 SQL 查詢並顯示結果
def search_data():
    keyword = entry.get()

    # 建立與資料庫的連接
    conn = connect_to_database()

    if conn:
        # 建立遊標
        cursor = conn.cursor()

        keyword = "HKTVMALL"

        cursor.execute("SELECT * FROM product_info WHERE sources = %s", (keyword,))

        # 取得查詢結果
        results = cursor.fetchall()

        # 關閉連接
        cursor.close()
        conn.close()

        # 清空表格
        for row in result_tree.get_children():
            result_tree.delete(row)

        # 在表格中顯示搜索結果
        if results:
            for row in results:
                result_tree.insert("", tk.END, values=row)
        else:
            result_text.insert(tk.END, "沒有找到相關資料。")

        # 執行計算
        calculate_result = len(results) * 2  # 假設這裡是一個簡單的計算示例

        # 清空計算結果文字區域
        calculate_text.delete("1.0", tk.END)

        # 顯示計算結果
        calculate_text.insert(tk.END, f"計算結果：{calculate_result}")

# 刪除選定的資料
def delete_data():
    selected_item = result_tree.selection()
    if selected_item:
        item_id = result_tree.item(selected_item)["values"][0]  # 假設ID欄位在第一列
        # 建立與資料庫的連接
        conn = connect_to_database()

        if conn:
            # 建立遊標
            cursor = conn.cursor()

            # 執行刪除資料的SQL語句
            cursor.execute("DELETE FROM product_info WHERE id = %s", (item_id,))

            # 提交資料庫事務
            conn.commit()

            # 關閉連接
            cursor.close()
            conn.close()

            # 從表格中刪除選定的行
            result_tree.delete(selected_item)

            result_text.insert(tk.END, "資料刪除成功。")
    else:
        result_text.insert(tk.END, "請選擇要刪除的資料。")

# 創建 GUI 視窗
window = tk.Tk()
window.title("資料搜索")
window.geometry("400x400")

# 創建資料庫連接按鈕
connect_button = tk.Button(window, text="連接資料庫", command=connect_to_database)
connect_button.pack()

# 創建搜索輸入框
entry = tk.Entry(window)
entry.pack()

# 創建搜索按鈕
search_button = tk.Button(window, text="搜索", command=search_data)
search_button.pack()

# 創建結果顯示區域
result_tree = ttk.Treeview(window, columns=("column1", "column2", "column3", "column4", "column5","column6","column7"))  # 設定表格的欄位
result_tree.pack()

result_tree.heading("#0", text="ID")
result_tree.heading("column1", text="ID")
result_tree.heading("column2", text="NAME")
result_tree.heading("column3", text="PRODUCER")
result_tree.heading("column4", text="CATEGORY")
result_tree.heading("column5", text="SOURCES")
result_tree.heading("column6", text="PAGE_URL")
result_tree.heading("column7", text="IMG_URL")

result_tree.column("#0", width=50)
result_tree.column("column1", width=100)
result_tree.column("column2", width=100)
result_tree.column("column3", width=100)
result_tree.column("column4", width=100)
result_tree.column("column5", width=100)
result_tree.column("column6", width=100)
result_tree.column("column7", width=100)

# 創建計算結果顯示區域
calculate_text = tk.Text(window, height=1, width=30)
calculate_text.pack()

# 創建刪除按鈕
delete_button = tk.Button(window, text="刪除", command=delete_data)
delete_button.pack()

# 創建結果提示文字區域
result_text = tk.Text(window)
result_text.pack()

# 啟動 GUI 應用程式
window.mainloop()

