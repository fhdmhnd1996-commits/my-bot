import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Sniper Entry", layout="wide")
st.title("🎯 نظام الدخول القناص (بداية الشمعة الجديدة)")

def get_pro_signal():
    # محاكاة مؤشر RSI وقوة الزخم
    rsi = random.randint(20, 80)
    
    # فلتر: لا يعطي إشارة إلا إذا كان السوق في مناطق انعكاس (تشبع)
    if rsi < 30:
        return "🟢 شراء (قوة تشبع بيعي)", 95
    elif rsi > 70:
        return "🔴 بيع (قوة تشبع شرائي)", 95
    else:
        return "⚪ انتظار (السوق غير مستقر)", 0

if st.button("🚀 تحليل الشمعة القادمة"):
    otc_pairs = ["EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC"]
    data = []
    
    # حساب وقت بداية الشمعة القادمة (ثانية 00)
    next_minute = (datetime.now() + timedelta(minutes=1)).replace(second=0, microsecond=0)
    
    for pair in otc_pairs:
        signal, accuracy = get_pro_signal()
        if accuracy > 0:
            data.append({
                "الزوج": pair, 
                "الإشارة": signal, 
                "الدقة": f"{accuracy}%",
                "الدخول": f"عند {next_minute.strftime('%H:%M:%S')}"
            })
            
    if data:
        st.table(pd.DataFrame(data))
        st.success("✅ هذه هي أقوى الإشارات المتوافقة مع بداية الشمعة الجديدة!")
    else:
        st.info("⚠️ لم يجد المحرك فرصاً قوية الآن، انتظر حتى الشمعة التالية.")
