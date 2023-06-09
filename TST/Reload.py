import requests
username = 'thespacetoolkit'
token = 'c2fc2b11e2a66d90fa8914de9520a23152f1dcd5'
domain_name = 'thespacetoolkit.pythonanywhere.com'
response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        username=username, domain_name=domain_name
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
