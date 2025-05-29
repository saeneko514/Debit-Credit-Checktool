import pandas as pd

# CSVを読み込み
df = pd.read_csv("journal_sample.csv")

# 金額列を数値型に変換
df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
df["Debit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)

# 伝票番号ごとの借方・貸方合計を計算
summary = df.groupby("Number")[["Debit", "Credit"]].sum().reset_index()

# 貸借差額を計算
summary["Diff"] = summary["Debit"] - summary["Credit"]

# バランスしていない伝票を抽出
unbalanced = summary[summary["Diff"] != 0]

# 結果を表示
if unbalanced.empty:
    print("✅ 全ての伝票で貸借が一致しています。")
else:
    print("⚠️ 貸借が一致していない伝票があります:")
    print(unbalanced)