from flask import Flask, request, jsonify # type: ignore
import pygame  # ใช้ pygame แทน playsound
import threading

app = Flask(__name__)

# ฟังก์ชันสำหรับเล่นเสียง
def play_alert_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("siren-alert-96052.mp3")  # ไฟล์เสียงต้องอยู่ในโฟลเดอร์เดียวกัน
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Error playing sound: {e}")

@app.route('/webhook', methods=['POST'])
def grafana_alert():
    try:
        # รับข้อมูลแจ้งเตือนจาก Grafana
        data = request.json
        alert_title = data.get("title", "No Title")
        alert_message = data.get("message", "No Message")
        alert_status = data.get("state", "No State")
        print(f"\n=== Alert Received ===\nTitle: {alert_title}\nMessage: {alert_message}\nState: {alert_status}\n")

        # เล่นเสียงแจ้งเตือน
        threading.Thread(target=play_alert_sound).start()

        return jsonify({"status": "success", "message": "Alert received"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)