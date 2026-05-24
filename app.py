import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Session Plan", layout="centered")
st.title("🎯 خطة الـ 10 صفقات القادمة")

# إعداد وقت البداية
if st.button("🚀 ابدأ استخراج جدول الجلسة"):
    start_time = datetime.now()
    
    st.write(f"### وقت بدء الجلسة: {start_time.strftime('%H:%M:%S')}")
    
    # إنشاء جدول الصفقات
    results = []
    for i in range(1, 11):
        # إضافة 3 دقائق لكل صفقة تالية
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        results.append({
            "الصفقة": i,
            "وقت الدخول": trade_time.strftime('%H:%M:%S'),
            "الحالة": "جاهز للمراقبة"
        })
    
    # عرض الجدول
    df_results = pd.DataFrame(results)
    st.table(df_results)
    
    st.success("هذا جدول صفقاتك للـ 30 دقيقة القادمة. التزم بالوقت بدقة!")

# ملاحظة: هذا الجدول للجدولة فقط. 
# للتحليل الفعلي لكل صفقة عند وقتها، سأدمج لك منطق التحليل في الكود القادم.
