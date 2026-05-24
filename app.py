# بدلاً من الزر في القائمة الجانبية، سنجعله في منتصف الواجهة ليكون أوضح
st.subheader("💡 اضغط هنا لبدء الرادار:")
if st.button("🚀 تحليل السوق الآن"):
    st.info(f"جاري تحليل حركة السعر على {pair}...")
    
    # محاكاة إشارة (سيتم استبدالها لاحقاً بمعادلات حقيقية)
    signal = random.choice(["🟢 شراء (CALL)", "🔴 بيع (PUT)"])
    confidence = random.randint(75, 98)
    
    st.subheader(f"نتيجة التحليل لزوج {pair}:")
    if "شراء" in signal:
        st.success(f"القرار: {signal} | نسبة النجاح: {confidence}%")
    else:
        st.error(f"القرار: {signal} | نسبة النجاح: {confidence}%")
        
    # إضافة الإشارة للسجل
    new_signal = {"الزوج": pair, "الإشارة": signal, "الثقة": f"{confidence}%"}
    st.session_state.signals.append(new_signal)
    st.rerun() # هذا الأمر سيجعل الصفحة تحدث نفسها لتظهر الإشارة فوراً في الجدول
