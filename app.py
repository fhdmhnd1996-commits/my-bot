import streamlit as st
import pandas as pd
import numpy as np
import random

# --- إعدادات النظام ---
st.set_page_config(page_title="Advanced SR + Chandelier System", layout="wide")
st.title("🎯 نظام الدمج الاحترافي: SR Breaks + Chandelier Exit")

# --- محاكاة المؤشرات ---
def get_market_data():
    # محاكاة بيانات السعر
    data = []
    for pair in ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC"]:
        price = random.uniform(1.0500, 1.1000)
        # SR Break: هل السعر اخترق مستوى؟
        sr_signal = random.choice(["Breakout Up", "Breakout Down", "None"])
        # Chandelier Exit: هل نحن في اتجاه صعودي أم هبوطي؟
        chandelier_trend = random.choice(["Bullish", "Bearish"])
        
        data.append({"Pair": pair, "Price": price, "SR_Signal": sr_signal, "Trend": chandelier_trend})
    return pd.DataFrame(data)

# --- منطق الدمج (هنا يكمن سر القوة) ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        # شرط الدخول: اختراق مقاومة (Breakout Up) + اتجاه صعودي (Bullish)
        if row['SR_Signal'] == "Breakout Up" and row['Trend'] == "Bullish":
            signal = "🟢 شراء قوي (تأكيد مزدوج)"
        # شرط الدخول: اختراق دعم (Breakout Down) + اتجاه هبوطي (Bearish)
        elif row['SR_Signal'] == "Breakout Down" and row['Trend'] == "Bearish":
            signal = "🔴 بيع قوي (تأكيد مزدوج)"
        else:
            signal = "⚪ انتظار (عدم توافق)"
            
        row['Final_Decision'] = signal
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 تشغيل نظام الدمج (SR + Chandelier)"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    st.table(final_df)
    
    st.markdown("""
    ### شرح استراتيجية الدمج:
    * **SR Breaks:** يحدد "نقطة الانفجار السعري".
    * **Chandelier Exit:** يحدد "الترند العام" ويحمي الصفقة من التذبذب.
    * **القوة:** لن يتم عرض إشارة دخول إلا إذا اتفق المؤشران معاً. 
    """)
    st.success("تم تحليل السوق بدمج المؤشرين.")

