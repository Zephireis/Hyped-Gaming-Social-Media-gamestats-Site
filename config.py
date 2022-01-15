from urllib import parse

TOKEN = "Mjg4MjU4MDEwNjEzMTUzODAy.WL07MQ.-mI3GE8_vP0Omw3jw3N-pbRDrGg"
CLIENT_SECRET = "iDR56osnkqYA51atkvjy2JqfuBMBaoU1"
REDIRECT_URI = "http://192.168.1.118:4444/oauth/callback"
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=288258010613153802&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify"
