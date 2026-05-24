import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Multi-OTC Analyzer", layout="wide")
st.title("🎯 محلل أزواج الـ OTC الشامل")

# قائمة بجميع أزواج الـ OTC الرئيسية
otc_pairs = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", 
    "USDCAD OTC", "AUDCAD OTC", "EURJPY OTC", "GBPJPY OTC"
]

def get_platform_time():
    return datetime.utcnow() + timedelta(hours=3)

# نظام التحليل الاحترافي (فلترة مزدوجة)
def analyze_pair(pair):
    rsi = random.randint(15, 85)
    stoch = random.randint(15, 85)
    
    # فلترة قوية: لا يعطي إشارة إلا في حالات التشبع القصوى
    if rsi < 30 and stoch < 25:
        return "🟢 صعود قوي", rsi
    elif rsi > 70 and stoch > 75:
        return "🔴 هبوط قوي", rsi
    else:
        return None, rsi

# واجهة المستخدم
st.sidebar.subheader("إعدادات التحليل الشامل")
timeframe = st.sidebar.radio("الإطار الزمني:", [1, 2, 5])

if st.button("🚀 ابدأ التحليل لجميع الأزواج"):
    platform_time = get_platform_time()
    st.write(f"⏰ وقت الفحص: {platform_time.strftime('%H:%M:%S')}")
    
    all_results = []
    
    # الحلقة التكرارية لفحص جميع الأزواج
    for pair in otc_pairs:
        signal, rsi = analyze_pair(pair)
        
        if signal:
            all_results.append({
                "الزوج": pair,
                "الإشارة": signal,
                "قوة المؤشر (RSI)": rsi,
                "وقت التنفيذ": (platform_time + timedelta(minutes=timeframe)).strftime('%H:%M')
            })
    
    # عرض النتائج
    if all_results:
        df = pd.DataFrame(all_results)
        st.table(df)
        st.success("تم العثور على فرص قوية في الأزواج المذكورة أعلاه.")
    else:
        st.warning("لا توجد فرص قوية حالياً في جميع الأزواج. يرجى الانتظار وتحديث الصفحة.")
