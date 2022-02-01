import requests, json

# Get refresh token from google drive api
# Generating a refresh token for DRIVE API calls using the OAuth playground
# https://www.youtube.com/watch?v=hfWe1gPCnzc
def getToken():
	oauth = 'https://www.googleapis.com/oauth2/v4/token' # Google API oauth url
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	data = {
        'grant_type': 'refresh_token',
        'client_id': '####',
        'client_secret': '####', 
        'refresh_token': '1//04I1SvbVE82b_CgYIARAAGAQSNwF-L9IrhJJEl4is_shr7-wYI4fQqy5vlBvi57-_HYBQ7xWk-QII655dmMoeqqlWXUOI6-oczJE',
    }

	token = requests.post(oauth, headers=headers, data=data)
	_key = json.loads(token.text)
	return _key['ya29.a0ARrdaM9AmBRm7xoDpKf6LOpl90CRd-1XOfYk7eTJEolf-lSireMIFlk4JIkY5tpI35TcNmLo3UJGgmI5cUbmlacHo8HgXqXCahGYZ-Hnjg0kFj_qs-VsTbt-wjat0wkGdEHn-Pguz8jZaJU1Y_j5kvJoKVzk']

# Upload files to google drive using access token
def upload2Drive(files):
	TOKEN_KEY = getToken()
	headers = {"Authorization": "Bearer "+TOKEN_KEY}
	upload = requests.post(
	    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
	    headers=headers,
	    files=files
	)
	print(upload.text)


if __name__ == '__main__':
	file = "sample.jpg" # change your file name
	
	para = {
	    "name": file, #file name to be uploaded
	    "parents": ["1S-gVNUWcxoeJY6JnQP98cIkA7qRscqC0"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
	}
	files = {
	    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
	    'file': ('image/jpg',open("./"+file, "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
	}

	upload2Drive(files)