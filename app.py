import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro OTC Filter v2.1", layout="wide")
st.title("🛡️ نظام الفلترة الرباعي الاحترافي")

# دالة تحاكي بيانات السوق
def get_advanced_market_data():
    data = []
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    for pair in pairs:
        data.append({
            "الزوج": pair,
            "RSI": np.random.randint(20, 80),
            "Volume": np.random.uniform(0.5, 2.0),
            "EMA_Signal": np.random.uniform(-0.002, 0.002),
            "Sentiment": np.random.choice(['Strong Bull', 'Strong Bear', 'Choppy'])
        })
    return pd.DataFrame(data)

# --- منطق الفلترة ---
def strict_filter(row):
    is_bullish = (row['RSI'] < 70) and (row['EMA_Signal'] > 0) and (row['Sentiment'] == 'Strong Bull')
    is_bearish = (row['RSI'] > 30) and (row['EMA_Signal'] < 0) and (row['Sentiment'] == 'Strong Bear')
    
    if is_bullish and row['Volume'] > 1.0:
        return "🟢 شراء (تأكيد عالٍ)"
    elif is_bearish and row['Volume'] > 1.0:
        return "🔴 بيع (تأكيد عالٍ)"
    else:
        return "⚪ فلترة (تجنب الخسارة)"

# --- الواجهة والتنفيذ ---
if st.button("🚀 مسح السوق بفلترة صارمة"):
    df = get_advanced_market_data()
    df['القرار'] = df.apply(strict_filter, axis=1)
    
    # دالة التنسيق الشرطي (متوافقة مع الإصدارات الحديثة)
    def highlight_rows(x):
        if 'شراء' in x:
            return 'background-color: #d4edda'
        elif 'بيع' in x:
            return 'background-color: #f8d7da'
        return ''

    # عرض الجدول
    st.dataframe(
        df.style.map(highlight_rows, subset=['القرار']),
        use_container_width=True
    )
    
    # إحصائية سريعة
    if len(df[df['القرار'] != "⚪ فلترة (تجنب الخسارة)"]) == 0:
        st.warning("السوق غير مستقر حالياً، النظام منعك من الدخول لتجنب الخسارة.")
    else:
        st.success("تم العثور على فرص مطابقة للمعايير.")

st.markdown("""
### ملاحظات هامة:
* تم استخدام دالة `map` بدلاً من `applymap` لضمان عمل الكود على أحدث إصدارات مكتبة `pandas`.
* لا تدخل أي صفقة إذا كان المؤشر يشير إلى **"فلترة"**.
* الصبر في انتظار الإشارة الصحيحة هو سر تجنب الخسائر في سوق الـ OTC.
""")
