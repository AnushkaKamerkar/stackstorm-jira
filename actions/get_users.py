from st2common.runners.base_action import Action
from requests.auth import HTTPBasicAuth
import requests
from flatten_dict import flatten

__all__ = [
    'GetJiraUserAction'
]

class GetJiraUserAction(Action):
	def run(self, accountId):
		email=self.config['email']
		token = self.config['api_token']
		base_url = self.config['url']
		
		url = base_url + "/rest/api/3/user/bulk"
		auth = HTTPBasicAuth(email, token)
		headers = {"Accept": "application/json"}
		query = {'accountId': accountId}
		response = requests.request("GET",url,headers=headers,params=query,auth=auth)
		result = flatten(response.json())
		print(type(result))
		return result

		
