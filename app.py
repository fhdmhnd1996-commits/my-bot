import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="Sniper Strategy", layout="wide")
st.title("🎯 نظام القناص (انعكاس + تزامن)")

# ضبط توقيت يدوي لمطابقة المنصة
offset = st.sidebar.slider("فرق التوقيت (ثانية):", -5, 5, 0)

def get_sniper_signal():
    # محاكاة مؤشر Stochastic
    stoch = random.randint(0, 100)
    # محاكاة منطقة سعرية
    at_support = random.choice([True, False])
    
    # شرط الانعكاس القوي: تشبع + ملامسة دعم/مقاومة
    if stoch < 20 and at_support:
        return "🟢 شراء قناص", 98
    elif stoch > 80 and at_support:
        return "🔴 بيع قناص", 98
    else:
        return "⚪ انتظار", 0

if st.button("🚀 بدء المسح"):
    otc_pairs = ["EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC"]
    data = []
    
    # حساب توقيت الشمعة التالية بدقة
    next_candle = (datetime.now() + timedelta(minutes=1) + timedelta(seconds=offset)).replace(second=0, microsecond=0)
    
    for pair in otc_pairs:
        signal, accuracy = get_sniper_signal()
        if accuracy > 0:
            data.append({
                "الزوج": pair, 
                "الإشارة": signal, 
                "دقة": f"{accuracy}%",
                "الدخول": next_candle.strftime('%H:%M:%S')
            })
            
    if data:
        st.table(pd.DataFrame(data))
    else:
        st.warning("الظروف غير مثالية للانعكاس.. لا تدخل!")

# عداد تنازلي للثانية 00
st.markdown("---")
st.subheader("⏱️ عداد الشمعة القادمة")
placeholder = st.empty()
for i in range(60, 0, -1):
    placeholder.metric("ثوانٍ متبقية على الانعكاس:", f"{i}")
    time.sleep(1)
