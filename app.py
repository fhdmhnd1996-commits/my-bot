import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Professional OTC Trading Plan", layout="wide")
st.title("🎯 خطة التداول الذكية (10 صفقات متتالية)")

# قائمة الأزواج
otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC"
]

# التحكم في وقت البدء
start_option = st.radio("متى تريد بدء الجلسة؟", ["الآن", "تحديد وقت يدوي"])
if start_option == "الآن":
    base_time = datetime.now()
else:
    # يمكنك إضافة إدخال لوقت يدوي هنا
    base_time = datetime.now()

if st.button("🚀 إنشاء جدول الصفقات"):
    data = []
    for i in range(1, 11):
        # صفقات بفاصل 3 دقائق
        trade_time = base_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[(i-1) % len(otc_list)]
        data.append([i, pair, trade_time.strftime('%H:%M:%S')])
    
    df = pd.DataFrame(data, columns=["رقم الصفقة", "الزوج", "وقت الدخول"])
    
    # تنسيق الجدول
    st.table(df.style.set_properties(**{'text-align': 'center'}))
    
    st.info("💡 نصيحة: إذا خسرت صفقتين متتاليتين، توقف فوراً عن إكمال الجدول حتى لو كان هناك صفقات متبقية.")

st.markdown("""
### 🛡️ قواعد الجلسة:
* **إدارة المخاطر:** لا تضع أكثر من 2-5% من رصيدك في الصفقة الواحدة.
* **الالتزام:** الجدول وُضع لتقليل التوتر، اتبع الترتيب بدقة.
* **المرونة:** إذا تحرك السوق بشكل غير طبيعي، لا تتردد في تخطي "الزوج" المذكور في الجدول.
""")
