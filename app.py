import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Session", layout="wide")
st.title("🎯 جدول صفقات الـ OTC (بالإشارات)")

# عرض الوقت الحالي
st.metric("⏰ الوقت الحالي", datetime.now().strftime("%H:%M"))

otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

if st.button("🚀 استخراج جدول الصفقات"):
    start_time = datetime.now().replace(second=0, microsecond=0)
    
    data = []
    for i in range(1, 11):
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[(i-1) % len(otc_list)]
        
        # وضع إشارة خضراء للصعود وحمراء للهبوط بالتناوب
        signal = "🟢 صعود (BUY)" if i % 2 != 0 else "🔴 هبوط (SELL)"
        
        data.append([i, pair, trade_time.strftime('%H:%M'), signal])
    
    # عرض الجدول
    df = pd.DataFrame(data, columns=["رقم الصفقة", "الزوج", "وقت الدخول", "نوع الإشارة"])
    st.table(df)
    
    st.success("الجدول جاهز! 🟢 صعود و 🔴 هبوط.")

if st.button("🔄 تحديث الوقت"):
    st.rerun()
