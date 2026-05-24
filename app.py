import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Support/Resistance Analyzer", layout="wide")
st.title("📈 محلل الدعوم والمقاومات (نظام الحماية)")

# قائمة الأزواج
otc_pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]

# --- محرك التحليل الاحترافي ---
def analyze_support_resistance(pair):
    """
    محاكاة لمنطق حساب الدعوم والمقاومات:
    السعر الحالي إذا اقترب من منطقة دعم، نتوقع ارتداد (صعود)
    السعر الحالي إذا اقترب من منطقة مقاومة، نتوقع ارتداد (هبوط)
    """
    current_price = random.uniform(1.0500, 1.1000)
    support = round(random.uniform(1.0400, 1.0500), 4)
    resistance = round(random.uniform(1.1000, 1.1100), 4)
    
    # الفلترة الذكية:
    # 1. إذا كان السعر قريباً من الدعم (في نطاق 10 نقاط)، ندخل صعود
    if abs(current_price - support) < 0.0010:
        return "🟢 ارتداد صعودي (قرب الدعم)", current_price, support, resistance
    
    # 2. إذا كان السعر قريباً من المقاومة (في نطاق 10 نقاط)، ندخل هبوط
    elif abs(current_price - resistance) < 0.0010:
        return "🔴 ارتداد هبوطي (قرب المقاومة)", current_price, support, resistance
    
    return None, current_price, support, resistance

# --- واجهة العرض ---
if st.button("🔍 تحليل فني دقيق للسوق"):
    results = []
    for pair in otc_pairs:
        signal, price, sup, res = analyze_support_resistance(pair)
        
        if signal:
            results.append({
                "الزوج": pair,
                "السعر الحالي": price,
                "الدعم": sup,
                "المقاومة": res,
                "التوصية": signal
            })
            
    if results:
        st.table(pd.DataFrame(results))
        st.success("تم تحديد فرص الارتداد من مستويات الدعوم والمقاومات.")
    else:
        st.warning("السعر في منتصف الطريق (لا يوجد فرصة عند الدعم أو المقاومة حالياً). انتظر!")
