from lib.base import BaseJiraAction

__all__ = [
    'GetJiraUserAction'
]


class GetJiraUserAction(BaseJiraAction):
	def run(self, accountId):
		url = "https://thrivecs.atlassian.net/rest/api/3/user/bulk"
		auth = HTTPBasicAuth("anushka@coditation.com", "rBC647X9WzvSUY3JZV15152F")
		headers = {"Accept": "application/json"}
		query = {'accountId': '5b4f0eb54351c62c0572b071'}
		response = requests.request("GET",url,headers=headers,params=query,auth=auth)
		print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
