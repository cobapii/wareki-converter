import streamlit as st

st.title("西暦→和暦変換")

year = st.number_input("西暦を入力", min_value=1868, max_value=2100, step=1)

if year >= 2019:
    era = f"令和{year - 2018}年"
elif year >= 1989:
    era = f"平成{year - 1988}年"
elif year >= 1926:
    era = f"昭和{year - 1925}年"
elif year >= 1912:
    era = f"大正{year - 1911}年"
elif year >= 1868:
    era = f"明治{year - 1867}年"
else:
    era = "明治以前"

st.write("和暦:", era)
