from dotenv import load_dotenv
import streamlit as st
load_dotenv(override=True)

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject= "AI"
# result =chat_model.invoke(subject+"에 대한 시를 써줘.")
# print(result.content)

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제:"+subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject+"에 대한 시를 써줘")
        st.write(result.content)