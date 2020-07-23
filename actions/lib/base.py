from jira import JIRA
from requests.auth import HTTPBasicAuth
import requests
import json

#  from st2common.runners.base_action import Action
__all__ = [
    'BaseJiraAction'
]


class Action(object):
	def __init__(self, config):
        	self.config = config


class BaseJiraAction(Action):
	def __init__(self, config):
		super(BaseJiraAction, self).__init__(config=config)
		self._client = self._get_client()

	def _get_client(self):
		config = self.config

		options = {'server': config['url'], 'verify': config['verify']}

		auth_method = config['auth_method']

		if auth_method == 'oauth':
		    rsa_cert_file = config['rsa_cert_file']
		    rsa_key_content = self._get_file_content(file_path=rsa_cert_file)

		    oauth_creds = {
		        'access_token': config['oauth_token'],
		        'access_token_secret': config['oauth_secret'],
		        'consumer_key': config['consumer_key'],
		        'key_cert': rsa_key_content
		    }

		    client = JIRA(options=options, oauth=oauth_creds)

		elif auth_method == 'basic':
		    email = config['email']		
		    token = config['api_token']
		    #auth = HTTPBasicAuth(email, token)
		    #return email,token

		else:
		    msg = ('You must set auth_method to either "oauth"',
		           'or "basic" your jira.yaml config file.')
		    raise Exception(msg)

		return email,token
		#return client

	def get_users(self,accountId):
		url = "https://thrivecs.atlassian.net/rest/api/3/user/bulk"
		#auth = HTTPBasicAuth("anushka@coditation.com", "xKfdFUrlzlpYg8KNBI1i4EC9")
		headers = {"Accept": "application/json"}
		#query = {'accountId': '5b4f0eb54351c62c0572b071'}
		query = accountId
		email,token = self._get_client()
		print(email, token)
		auth = HTTPBasicAuth(email, token)
		response = requests.request("GET",url,headers=headers,params=query,auth=auth)
		#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
		return response.text

	def _get_file_content(self, file_path):
		with open(file_path, 'r') as fp:
		    content = fp.read()

		return content
