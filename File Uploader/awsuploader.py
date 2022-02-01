import boto3
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path= filedialog.askopenfile().name


s3_client = boto3.client('s3')

response = s3_client.upload_file(file_path ,'my-bucket-7653854310', file_path[-8]  )
print(response)

