from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from requests import Session

# Source for wskeys https://platform.worldcat.org/wskey/

# 'Library metadata including WorldCatMetadataAPI'
client_id = r'[Add client id here]'
client_secret = r'[add client secret here]'

token_url='https://oauth.oclc.org/token'

scope = ['WorldCatMetadataAPI:manage_bibs']

auth = HTTPBasicAuth(client_id, client_secret)

client = BackendApplicationClient(client_id=client_id, scope=scope)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, auth=auth, include_client_id=True)

print("Here is the token:\n")
print(token)

s = Session()
s.headers.update({"Authorization": f'Bearer {token["access_token"]}'})

response = s.get("https://metadata.api.oclc.org/worldcat/manage/bibs/1354771677")
#This one has a lot of 019s
#response = s.get("https://metadata.api.oclc.org/worldcat/manage/bibs/227919110")

print("Here is the response:\n")
print(response.text)

#Here is how to test the old Worldcat Search API v.1:
#https://worldcat.org/webservices/catalog/content/227919110?servicelevel=full&wskey=[put the wskey here]
