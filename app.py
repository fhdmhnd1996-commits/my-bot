    @staticmethod
    def apply_strategy(df):
        # 1. زيادة حساسية EMA
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        
        # 2. تحسين دقة RSI
        delta = df['Close'].diff()
        gain = delta.clip(lower=0).rolling(window=14).mean()
        loss = (-delta.clip(upper=0)).rolling(window=14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain / loss)))
        
        # 3. إشارة أقوى: شرط "الزخم" (Momentum)
        # الإشارة فقط إذا كان هناك فرق واضح بين EMA9 و EMA21
        df['Signal'] = 'Wait'
        
        # شراء: تقاطع صاعد + RSI تحت 35 (تشبع بيعي)
        df.loc[(df['EMA9'] > df['EMA21']) & (df['RSI'] < 35), 'Signal'] = 'BUY'
        
        # بيع: تقاطع هابط + RSI فوق 65 (تشبع شرائي)
        df.loc[(df['EMA9'] < df['EMA21']) & (df['RSI'] > 65), 'Signal'] = 'SELL'
        
        return df
