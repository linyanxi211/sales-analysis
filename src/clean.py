import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_CSV = ROOT / "data" / "raw" / "Sample_Superstore.csv"

def load_clean() -> pd.DataFrame:
    df = pd.read_csv(RAW_CSV, encoding = "latin-1")

    df["Order Date"] = pd.to_datetime(df["Order Date"], format = "%m/%d/%Y")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format = "%m/%d/%Y")

    return df

if __name__ == "__main__":
    df = load_clean()

    out = ROOT / "data" / "processed" / "superstore_clean.csv"
    out.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(out, index=False, encoding="utf-8")

    print(f"已写出 {out}")
    print(f"        {len(df):,} 行 × {df.shape[1]} 列")