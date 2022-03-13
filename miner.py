from requests.auth import HTTPDigestAuth
import requests
import sys


addr = 'http://192.168.0.'

end = '/cgi-bin/minerStatus.cgi'

for i in range(2,255):

	url = addr+str(i)+end

	try:
		req = requests.get(url, auth=HTTPDigestAuth(user, password), timeout=0.1)

	except:
		print(f'fail {url}', flush=True)# flush for visual

	else:
		print(f'{req} {url}')# no flushing
		break


