import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Pro OTC Multi-Analyzer", layout="wide")
st.title("🎯 نظام التداول الرباعي المطور (النسخة الاحترافية)")

# --- دالة التحليل الفني (محاكاة دقيقة) ---
def analyze_market():
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    for pair in pairs:
        # محاكاة مؤشرات فنية
        rsi = np.random.randint(20, 80)
        ema = np.random.choice([1, -1])  # اتجاه الصعود أو الهبوط
        volume_strength = np.random.uniform(0.5, 2.0)
        
        # منطق اتخاذ القرار
        if rsi < 40 and ema == 1 and volume_strength > 1.2:
            decision = "🟢 شراء قوي"
        elif rsi > 60 and ema == -1 and volume_strength > 1.2:
            decision = "🔴 بيع قوي"
        else:
            decision = "⚪ انتظار"
            
        data.append({
            "الزوج": pair,
            "RSI": rsi,
            "الاتجاه": "صاعد" if ema == 1 else "هابط",
            "السيولة": round(volume_strength, 2),
            "القرار": decision,
            "وقت الدخول (UTC+3)": (datetime.utcnow() + timedelta(hours=3)).strftime("%H:%M")
        })
    return pd.DataFrame(data)

# --- واجهة المستخدم ---
st.sidebar.header("🛠️ إعدادات التحكم")
if st.sidebar.button("🚀 تحديث تحليل السوق"):
    df = analyze_market()
    
    # التنسيق الشرطي
    def color_decision(val):
        if 'شراء' in val: return 'background-color: #d4edda; color: #155724; font-weight: bold'
        if 'بيع' in val: return 'background-color: #f8d7da; color: #721c24; font-weight: bold'
        return ''

    styled_df = df.style.map(color_decision, subset=['القرار'])
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    # فحص الفرص
    opportunities = df[df['القرار'] != "⚪ انتظار"]
    if not opportunities.empty:
        st.success(f"تم العثور على {len(opportunities)} فرص متاحة الآن!")
    else:
        st.warning("السوق غير مستقر، لا توجد إشارات دخول حالياً.")

# --- قسم التعليمات (إدارة المخاطر) ---
st.markdown("""
---
### 🛡️ قواعد التداول الذهبية (لتقليل الخسائر):
1. **الالتزام بالفلترة:** لا تدخل أي صفقة إذا لم تكن الإشارة "شراء/بيع قوي".
2. **إدارة رأس المال:** لا تخاطر بأكثر من 2% من رصيدك في الصفقة الواحدة.
3. **توقيت الصفقة:** تأكد أن وقت دخولك يطابق وقت المنصة (UTC+3) الموضح في الجدول.
4. **وقف التداول:** إذا خسرت صفقتين متتاليتين، أغلق البرنامج وخذ استراحة لمدة ساعة.
""")

# مؤشر توقيت حي
st.sidebar.write("---")
st.sidebar.write(f"🕒 توقيت المنصة الحالي: **{(datetime.utcnow() + timedelta(hours=3)).strftime('%H:%M:%S')}**")
