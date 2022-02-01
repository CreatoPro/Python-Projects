import requests
import base64
import json


params = {
                "grant_type": "password",
                "client_id": clinet_id,
                "client_secret":client_secret,
                "refresh_token":refresh_token 
        }