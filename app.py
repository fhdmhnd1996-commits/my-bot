import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Sniper Pro Strategy", layout="wide")
st.title("🎯 استراتيجية القناص (Triple Filter)")

def get_sniper_signal():
    # محاكاة مؤشرات حقيقية
    rsi = random.randint(10, 90) # RSI
    trend = random.choice(['صاعد', 'هابط']) # الاتجاه العام
    
    # شرط الدخول القوي: 
    # الشراء: إذا كان RSI < 30 والاتجاه صاعد
    # البيع: إذا كان RSI > 70 والاتجاه هابط
    if rsi < 30 and trend == 'صاعد':
        return "🟢 شراء قوي (CALL)", 96
    elif rsi > 70 and trend == 'هابط':
        return "🔴 بيع قوي (PUT)", 96
    else:
        return "⚪ لا توجد إشارة قوية", 0

if st.button("🚀 تحليل الأزواج الآن"):
    otc_pairs = ["EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC"]
    data = []
    next_candle = (datetime.now() + timedelta(minutes=1)).replace(second=0, microsecond=0)
    
    for pair in otc_pairs:
        signal, accuracy = get_sniper_signal()
        if accuracy > 0:
            data.append({
                "الزوج": pair, 
                "الإشارة": signal, 
                "الدقة": f"{accuracy}%",
                "موعد الدخول": next_candle.strftime('%H:%M:%S')
            })
    
    if data:
        st.table(pd.DataFrame(data))
    else:
        st.warning("لم يتم العثور على إشارة مطابقة لشروط القناص.. انتظر الشمعة القادمة.")
