# --- تحديث المحرك الآمن ---
if st.button("🚀 تشغيل المحرك والتحليل"):
    try:
        engine = TradingEngine()
        df = engine.get_data(ticker)
        
        # التأكد من أن البيانات ليست فارغة
        if df is not None and not df.empty:
            df = engine.apply_strategy(df)
            
            # التأكد من وجود بيانات كافية للحساب
            if len(df) > 21:
                last = df.iloc[-1]
                st.write(f"### السعر الحالي: {last['Close']:.5f}")
                st.write(f"### RSI: {last['RSI']:.2f}")
                
                # منطق الدخول
                if last['EMA9'] > last['EMA21'] and last['RSI'] < 30:
                    st.success("🟢 إشارة شراء قوية (Buy)")
                elif last['EMA9'] < last['EMA21'] and last['RSI'] > 70:
                    st.error("🔴 إشارة بيع قوية (Sell)")
                else:
                    st.warning("⚪ لا توجد إشارة مطابقة للمعايير.")
            else:
                st.error("⚠️ بيانات السوق غير كافية حالياً، يرجى الانتظار.")
        else:
            st.error("❌ فشل في جلب بيانات الزوج، تأكد من الرمز (Ticker).")
            
    except Exception as e:
        st.error(f"حدث خطأ تقني: {e}")
