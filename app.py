import streamlit as st
import pandas as pd
from io import BytesIO

st.title("💰 貸借一致チェックツール")
st.write("仕訳データ（CSV）をアップロードして、伝票ごとの貸借が一致しているかを確認できます。")

# CSVアップロード
uploaded_file = st.file_uploader("📤 CSVファイルを選択", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ ファイルを読み込みました。")

        # 数値変換
        df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
        df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)

        if st.button("🧮 貸借チェック開始"):
            # グループ集計
            summary = df.groupby("Number")[["Debit", "Credit"]].sum().reset_index()
            summary["Diff"] = summary["Debit"] - summary["Credit"]

            unbalanced = summary[summary["Diff"] != 0]

            if unbalanced.empty:
                st.success("🎉 全ての伝票で貸借が一致しています！")
            else:
                st.warning("⚠️ 一致していない伝票があります：")
                st.dataframe(unbalanced)

                # Excel出力用のBytesIO作成
                output = BytesIO()
                with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                    unbalanced.to_excel(writer, index=False, sheet_name="Unbalanced")
                    writer.save()
                st.download_button(
                    label="📥 不一致伝票をExcelでダウンロード",
                    data=output.getvalue(),
                    file_name="unbalanced_entries.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    except Exception as e:
        st.error(f"❌ エラーが発生しました: {e}")