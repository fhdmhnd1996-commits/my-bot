import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Professional OTC Session", layout="wide")
st.title("🎯 جدول صفقات الـ OTC الاحترافي")

# قائمة الـ 20 زوجاً
otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

# اختيار وقت البدء
st.subheader("إعدادات الجلسة")
col1, col2 = st.columns(2)
with col1:
    start_hour = st.number_input("ساعة البدء (24 ساعة)", min_value=0, max_value=23, value=datetime.now().hour)
with col2:
    start_minute = st.number_input("دقيقة البدء", min_value=0, max_value=59, value=datetime.now().minute)

if st.button("🚀 إنشاء جدول الصفقات بالدقيقة"):
    # تحديد وقت البدء
    start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    
    st.write(f"### وقت بدء الجلسة: {start_time.strftime('%H:%M')}")
    
    data = []
    for i in range(1, 11):
        # صفقات بفاصل 3 دقائق
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[(i-1) % len(otc_list)]
        data.append([i, pair, trade_time.strftime('%H:%M')]) # التوقيت بالدقيقة فقط
    
    # عرض الجدول بدون استخدام style.applymap لتجنب الخطأ
    df = pd.DataFrame(data, columns=["رقم الصفقة", "الزوج", "وقت الدخول"])
    st.table(df)
    
    st.success("الجدول جاهز! التزم بالدخول في الوقت المحدد.")

st.markdown("""
### 🛡️ قواعد الجلسة لتقليل الخسائر:
* **إدارة المخاطر:** لا تضع أكثر من 2% من رصيدك في الصفقة الواحدة.
* **الالتزام:** إذا خسرت صفقتين متتاليتين، **توقف فوراً**.
* **الدقة:** أدخل الصفقة في بداية الدقيقة الموضحة في الجدول.
""")
