/**
 * كود موحد للتحليل: توقيت UTC+3 + تحديد حالة السوق (OTC)
 */

function getMarketInfo() {
    // 1. حساب الوقت (UTC + 3)
    let now = new Date();
    let utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    let platformTime = new Date(utc + (3600000 * 3));
    
    // 2. التحقق من سوق OTC (السبت والأحد)
    let day = platformTime.getDay();
    let isOTC = (day === 0 || day === 6);
    
    return {
        time: platformTime.toLocaleTimeString('en-GB', { hour12: false }),
        isOTC: isOTC
    };
}

function runAnalysis() {
    const market = getMarketInfo();
    
    console.log("---");
    console.log("الوقت الحالي (UTC+3): " + market.time);
    console.log("حالة السوق: " + (market.isOTC ? "OTC (عطلة نهاية الأسبوع)" : "سوق عادي"));

    // 3. منطق التحليل الموحد
    if (market.isOTC) {
        // ضع هنا خوارزمية التحليل الخاصة بـ OTC
        console.log("جاري تشغيل تحليل صفقات OTC...");
        analyzeOTC(); 
    } else {
        // ضع هنا خوارزمية التحليل للسوق العادي
        console.log("جاري تشغيل تحليل السوق العادي...");
        analyzeNormal();
    }
}

// دوال التحليل الفارغة (ضع منطق التحليل الخاص بك بداخلها)
function analyzeOTC() {
    // مثال: إضافة شرط للـ OTC
    console.log("التحليل الخاص بـ OTC نشط الآن.");
}

function analyzeNormal() {
    // مثال: إضافة شرط للسوق العادي
    console.log("التحليل الخاص بالسوق العادي نشط الآن.");
}

// بدء التشغيل التلقائي كل ثانية
setInterval(runAnalysis, 1000);
