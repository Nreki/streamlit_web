import streamlit as st
import pandas as pd


#페이지 기본 설정
st.set_page_config(
    page_icon=":classical_building:",
    page_title="공연 및 전시 정보 사이트",
    layout="wide"
)

st.sidebar.title('Select Year')

select_year = st.sidebar.selectbox(
    '연도를 선택해주세요',
    [2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010]
)

st.sidebar.title('Select Month')

select_month = st.sidebar.selectbox(
    '월을 선택해주세요',
    [1,2,3,4,5,6,7,8,9,10,11,12]
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("공연 및 전시 정보")
st.subheader(str(select_year)+"년 "+str(select_month)+"월 공연 및 전시 정보")

import pandas as pd

df=pd.read_csv('data/concert_data_20231024.csv', encoding='cp949')
df=df.sort_values(by=["시작일"], ascending=True)
df.drop(['url','등록일'] , axis=1,inplace=True)
df['시작일']=pd.to_datetime(df['시작일'])
df = df.fillna('-')

tmp_df = df[(df['시작일'].dt.year== select_year)&(df['시작일'].dt.month== select_month)]
tmp_df['시작일'] = tmp_df['시작일'].dt.strftime("%Y-%m-%d")
tmp_df.reset_index(drop=True, inplace=True)

st.table(tmp_df)