import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_CSV = ROOT / "data" / "raw" / "Sample_Superstore.csv"

def load_clean() -> pd.DataFrame:
    df = pd.read_csv(RAW_CSV, encoding = "latin-1")

    df["Order Date"] = pd.to_datetime(df["Order Date"], format = "%m/%d/%Y")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format = "%m/%d/%Y")

    return df