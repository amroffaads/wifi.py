import subprocess
import requests
import json

# رابط الديسكورد الخاص بك
webhook_url = "https://discord.com/api/webhooks/1452755782377406586/_G5h9Irx3g3Uw7YgVCmvWVBSh0ctHx-cR_e1hbTrJk7p_TTqP4VwlHeeThuoaMhzdsta"

def get_wifi_name():
    try:
        # أمر للحصول على تفاصيل الشبكة في ويندوز
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8', errors="ignore")
        for line in data.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return "لا يمكن تحديد اسم الشبكة"

wifi_name = get_wifi_name()

# تجهيز الرسالة للديسكورد
payload = {
    "content": f"📡 **جهاز ابنك متصل الآن بشبكة:** {wifi_name}"
}

# إرسال البيانات
requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
