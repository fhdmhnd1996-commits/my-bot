            # التحقق عند إغلاق الشمعة (استخدام الشمعة قبل الأخيرة)
            # لأن الشمعة الحالية لا تزال تتحرك
            last_closed = df.iloc[-2] 
            last_rsi = rsi.iloc[-2]
            
            # وقت إغلاق الشمعة
            close_time = df.index[-2].strftime('%H:%M:%S')
            
            if last_closed['EMA9'] > last_closed['EMA21'] and last_rsi < 35:
                results.append(f"🟢 {name}: دخول شراء عند {close_time} (RSI: {last_rsi:.1f})")
            elif last_closed['EMA9'] < last_closed['EMA21'] and last_rsi > 65:
                results.append(f"🔴 {name}: دخول بيع عند {close_time} (RSI: {last_rsi:.1f})")
