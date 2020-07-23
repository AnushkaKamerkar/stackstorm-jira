from st2common.runners.base_action import Action
from requests.auth import HTTPBasicAuth
import requests

__all__ = [
    'GetJiraWorkflowAction'
]

class GetJiraWorkflowAction(Action):
	def run(self):
		email=self.config['email']
		token = self.config['api_token']
		base_url = self.config['url']
		
		url = base_url + "/rest/api/3/workflow/search"
		auth = HTTPBasicAuth(email, token)
		headers = {"Accept": "application/json"}
		response = requests.request("GET",url,headers=headers,auth=auth)
		result = (response.json())		
		return result["values"]

