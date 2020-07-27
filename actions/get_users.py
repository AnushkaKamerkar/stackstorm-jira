from st2common.runners.base_action import Action
from requests.auth import HTTPBasicAuth
import requests
import json


__all__ = [
    'GetJiraUserAction'
]

class GetJiraUserAction(Action):
	def flatten_dict(dd, separator ='_', prefix =''): 
	    return { prefix + separator + k if prefix else k : v 
		     for kk, vv in dd.items() 
		     for k, v in flatten_dict(vv, separator, kk).items() 
		     } if isinstance(dd, dict) else { prefix : dd } 


	def run(self, accountId):
		email=self.config['email']
		token = self.config['api_token']
		base_url = self.config['url']
		
		url = base_url + "/rest/api/3/user/bulk"
		auth = HTTPBasicAuth(email, token)
		headers = {"Accept": "application/json"}
		query = {'accountId': accountId}
		response = requests.request("GET",url,headers=headers,params=query,auth=auth)
		
		result = response.json()
		result1=result["values"]
		for i in result1:
			res_dct = dict(i)
			

		return res_dct



		
