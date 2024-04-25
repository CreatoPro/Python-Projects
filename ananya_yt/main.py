import subprocess


# Define the command to run upload.py
command = [
    "python", 
    "upload.py", 
    "--file=test-1.mp4",
    "--title=Summer vacation in California Public",
    "--description=Had fun surfing in Santa Cruz", 
    "--keywords=surfing,Santa Cruz", 
    "--category=22", 
    "--privacyStatus=private",
    "--playlist=PLZBVF8bQk1LiatvyyX58xXJLrGdkjec3g"
]

# Execute the command
subprocess.run(command)