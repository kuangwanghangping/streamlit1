import streamlit as st
import pandas as pd
st.write("## 早上好")
st.write("# 早上好")
st.write("早上好")
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [20, 21, 19, 22, 20],
    '成绩': [85, 90, 88, 79, 92]
}
# 创建DataFrame
df = pd.DataFrame(data)
st.dataframe(df)
st.image("./tupian.png",width=200)
a = 0
clicked = st.button("加一")
if "a" not in st.session_state:
    st.session_state.a=0
if clicked:
    st.session_state.a+=1
st.write(st.session_state.a)