<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <style>
        body { font-family: sans-serif; background: #2c3e50; color: white; padding: 10px; }
        .control-panel { display: flex; flex-direction: column; gap: 10px; }
        button { padding: 15px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
        .btn-buy { background: #27ae60; color: white; }
        .btn-sell { background: #c0392b; color: white; }
        #price-display { font-size: 20px; text-align: center; margin: 10px 0; }
    </style>
</head>
<body>

    <div class="control-panel">
        <div id="price-display">السعر: جارٍ الرصد...</div>
        <button class="btn-buy" onclick="trade('CALL')">شراء (CALL)</button>
        <button class="btn-sell" onclick="trade('PUT')">بيع (PUT)</button>
    </div>

    <script>
        // كود التواصل مع تطبيق Kodular
        function trade(action) {
            // هنا نضع كود الـ JavaScript الخاص بالمنصة للضغط على الزر
            alert("تم تنفيذ أمر: " + action);
        }

        // تحديث السعر (يتم ربطه لاحقاً بـ WebViewString)
        setInterval(() => {
            let currentPrice = "1.02150"; // هنا نضع كود جلب السعر من صفحة المنصة
            document.getElementById('price-display').innerText = "السعر: " + currentPrice;
        }, 1000);
    </script>
</body>
</html>
