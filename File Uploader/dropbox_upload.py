import dropbox
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
computer_path= filedialog.askopenfile().name
file_name = os.path.basename(computer_path)



dropbox_access_token= "9ugkmnZ-p0EAAAAAAAAAAar1vl1eaSbxNyzNOjIvh9GGx-kPvZZBQSoVfu-JpZRf"    #Enter your own access token
dropbox_path= f"/pythonuploader16073/{file_name}"


client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))

