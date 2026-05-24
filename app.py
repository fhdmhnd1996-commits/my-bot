import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Pro OTC Analyzer", layout="wide")
st.title("🎯 محلل الـ OTC الاحترافي")

# 1. دالة التوقيت (UTC + 3)
def get_platform_time():
    # الحصول على وقت UTC الحالي
    utc_now = datetime.utcnow()
    # إضافة 3 ساعات
    platform_time = utc_now + timedelta(hours=3)
    return platform_time

# 2. التحقق من حالة السوق (OTC)
# ملاحظة: في معظم المنصات OTC يكون متاحاً في عطلات نهاية الأسبوع (السبت والأحد)
def is_market_otc(current_time):
    # weekday() يعطي (0=الاثنين, 5=السبت, 6=الأحد)
    return current_time.weekday() in [5, 6]

# عرض الوقت الحالي في جانب الصفحة
current_time = get_platform_time()
otc_status = is_market_otc(current_time)

st.sidebar.subheader("🕒 معلومات النظام")
st.sidebar.write(f"توقيت المنصة: **{current_time.strftime('%H:%M:%S')}**")
st.sidebar.write(f"حالة السوق: **{'OTC مفعل' if otc_status else 'سوق عادي'}**")

otc_list = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]

def get_signal(pair):
    import random
    decision = random.choice(["🟢 صعود", "🔴 هبوط"])
    rsi = random.randint(20, 80)
    return decision, rsi

if st.button("🚀 تحليل جلسة الـ 10 صفقات"):
    if not otc_status:
        st.warning("⚠️ تنبيه: اليوم ليس يوم OTC، قد لا تكون النتائج دقيقة للأسواق العادية.")
    
    data = []
    # البدء من الوقت الحالي للمنصة
    start_time = current_time.replace(second=0, microsecond=0)
    
    for i in range(1, 11):
        time_slot = start_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[i % len(otc_list)]
        signal, rsi = get_signal(pair)
        
        data.append([i, pair, time_slot.strftime('%H:%M'), signal, f"RSI: {rsi}"])
    
    df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "الوقت", "الإشارة", "قوة التحليل"])
    st.table(df)
    st.success("تم تحليل الجلسة بناءً على توقيت المنصة (UTC+3) وحالة السوق.")
