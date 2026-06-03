import streamlit as st

st.set_page_config(layout="wide", page_title="Alnze Trading Bot")

st.title("📈 لوحة تحكم Alnze Trading")

# رابط المنصة
url = "https://pocketoption.com/en/login/"

# استخدام iframe لعرض المنصة داخل التطبيق
st.markdown(
    f'<iframe src="{url}" width="100%" height="800px"></iframe>',
    unsafe_allow_html=True
)

st.sidebar.success("المنصة مفعلة داخل التطبيق")
