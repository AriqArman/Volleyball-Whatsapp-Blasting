# from __future__ import print_function

# from apiclient import discovery
# from httplib2 import Http
# from oauth2client import client, file, tools

# SCOPES = "https://www.googleapis.com/auth/forms.body.readonly"
# DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

# store = file.Storage('token.json')
# creds = None
# if not creds or creds.invalid:
#     flow = client.flow_from_clientsecrets('client_secret_242286434503-rf804r008i4ol8gi2qdksh4m0undbv0g.apps.googleusercontent.com.json', SCOPES)
#     creds = tools.run_flow(flow, store)
# service = discovery.build('forms', 'v1', http=creds.authorize(
#     Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# # Prints the title of the sample form:
# form_id = '14J9HeiY29YJhLHUAd6_3AuFgDnLhtF3ge4smrQAqeNA'
# result = service.forms().get(formId=form_id).execute()
# print(result)

from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Prints the responses of your specified form:
form_id = '14J9HeiY29YJhLHUAd6_3AuFgDnLhtF3ge4smrQAqeNA'
result = service.forms().responses().list(formId=form_id).execute()
print(result)