# 将 csv 变成数据库

from src.clean import load_clean
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    processed_db = ROOT / "data" / "processed" / "superstore.db"

    # 打开数据库文件
    con = sqlite3.connect(processed_db)

    # 把DataFrame 写成表
    df = load_clean()
    df.to_sql("superstore", con, index = False, if_exists="replace")

    print(f"{len(df):,}行")

    # 用完关掉
    con.close()