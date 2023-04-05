import speech_recognition as sr
import time
import pyautogui


# 創建一個Recognizer物件
r = sr.Recognizer()
r.dynamic_energy_threshold = True  # 啟用自動能量閾值調整
# 使用麥克風錄音
with sr.Microphone() as source:
    print("請說話，輸入q結束：")
    # 持續錄音，直到按下Q鍵
    while True:
        audio = r.listen(source)

        try:
            # 使用Google Web Speech API辨識語音
            text = r.recognize_google(audio, language='zh-TW')
            print(f"辨識結果：{text}")

            # 將辨識結果存成txt檔案
            with open("output.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")
                print("語音辨識結果已寫入output.txt檔案")
                pyautogui.press('enter')  # 模擬按下 Enter 鍵
        except sr.UnknownValueError:
            print("無法辨識語音")
        except sr.RequestError as e:
            print("無法取得Google Web Speech API的回應",e)

        # 持續錄音，直到按下Q鍵
        if input("輸入q結束，按下Enter繼續語音辨識") == "q":
            break