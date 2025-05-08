import random # ใช้สำหรับ สุ่มค่า
import string
import requests # ส่งคำขอ HTTP เช่น GET, POST เพื่อเชื่อมต่อกับ API
import os
import time

def ngl():
    # สุ่ม path ใช้เพื่อจำแนกคำขอแต่ละรายการว่าไม่ซ้ำกัน
    def deviceId():
        characters = string.ascii_lowercase + string.digits
        parts = [
            ''.join(random.choices(characters, k=8)),
            ''.join(random.choices(characters, k=4)),
            ''.join(random.choices(characters, k=4)),
            ''.join(random.choices(characters, k=4)),
            ''.join(random.choices(characters, k=12))
        ]
        return f"{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}-{parts[4]}"

    #  หลบการบล็อก/ป้องกันสแปม  ปลอมตัวเป็นเบราว์เซอร์/อุปกรณ์อื่น
    def UserAgent():
       with open('user-agents.txt', 'r') as file:
            user_agents = file.readlines() #  อ่านทุกบรรทัดในไฟล์
            random_user_agent = random.choice(user_agents).strip() # สุ่มเลือก 1 บรรทัด และลบช่องว่าง/ขึ้นบรรทัด
           
            return random_user_agent
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
        █████╗ ██████╗ ████████╗██╗   ██╗    
        ██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝    
        ███████║██████╔╝   ██║    ╚████╔╝     
        ██╔══██║██╔══██╗   ██║     ╚██╔╝      
        ██║  ██║██║  ██║   ██║      ██║       
        ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ██    ██    ██
    """)

    username = input("ชื่อ ngl ไม่ใช่ลิ้ง: ")
    message = input("ข้อความ: ")
    count = int(input("จำนวน: "))
    delay = int(input("delay :"))

    for i in range(count):
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': f'{UserAgent()}',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': f'https://ngl.link/{username}',
        }
        
        data = {
            'username': username,
            'question': message,
            'deviceId': deviceId()
        }

        try:
            response = requests.post('https://ngl.link/api/submit', 
                headers=headers, 
                data=data, 
                timeout=10
            )
            
            if response.status_code == 200:
                i += 1
                print(f"[+] Send => {i}")
                time.sleep(delay)
            else:
                print("[-] Not Send")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error: {str(e)}")
ngl()
