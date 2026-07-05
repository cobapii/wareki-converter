import streamlit as st

st.title("西暦⇔和暦変換")

# あなたの生年月日
birth_year = 1968

mode = st.radio(
    "変換方向を選択",
    ["西暦→和暦", "和暦→西暦"]
)

# 西暦→和暦
if mode == "西暦→和暦":

    year = st.number_input(
        "西暦を入力",
        min_value=1868,
        max_value=2100,
        step=1
    )

    if year >= 2019:
        era = f"令和{year - 2018}年"
    elif year >= 1989:
        era = f"平成{year - 1988}年"
    elif year >= 1926:
        era = f"昭和{year - 1925}年"
    elif year >= 1912:
        era = f"大正{year - 1911}年"
    else:
        era = f"明治{year - 1867}年"

    age = year - birth_year

    st.success(f"和暦：{era}")
    st.info(f"小林忍の年齢：{age}歳")

# 和暦→西暦
else:

    era = st.selectbox(
        "元号を選択",
        ["令和", "平成", "昭和", "大正", "明治"]
    )

    wareki_year = st.number_input(
        "年を入力",
        min_value=1,
        max_value=99,
        step=1
    )

    if era == "令和":
        year = wareki_year + 2018
    elif era == "平成":
        year = wareki_year + 1988
    elif era == "昭和":
        year = wareki_year + 1925
    elif era == "大正":
        year = wareki_year + 1911
    else:
        year = wareki_year + 1867

    age = year - birth_year

    st.success(f"西暦：{year}年")
    st.info(f"小林忍の年齢：{age}歳")
