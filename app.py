def wareki(year):

    if year >= 2019:
        era="令和"
        era_year=year-2018

    elif year >=1989:
        era="平成"
        era_year=year-1988

    elif year >=1926:
        era="昭和"
        era_year=year-1925

    elif year >=1912:
        era="大正"
        era_year=year-1911

    elif year >=1868:
        era="明治"
        era_year=year-1867

    else:
        return "明治以前"

    if era_year==1:
        return f"{era}元年"

    return f"{era}{era_year}年"


st.title("西暦→和暦変換")

year=st.number_input(
    "西暦入力",
    min_value=1868,
    value=2026
)

if st.button("変換"):

    st.success(
        f"{year}年 → {wareki(year)}"
    )
