import json
import requests
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()



file_path= filedialog.askopenfile().name
file_name = os.path.basename(file_path)

params = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
        }



headers = {"Authorization": "Bearer ya29.a0ARrdaM_Dt_vsmLjdsCD2pBF5-aNBsEnZ9vRMhNPBkuu_sbq8y5HafUvuONE5CxTwUmCqHpf_c0Z5y0nVpQLMpu_NVb-9RR1cXfx0xDhpwyRzo3C-G_EC6B8bw1RE6yb-TqP-d3mAVyykvmxVzQX4Vk8q_DhT"}
para = {
    "name": file_name,
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open(file_path, "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)



