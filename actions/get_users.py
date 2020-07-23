from lib.base import BaseJiraAction
from requests.auth import HTTPBasicAuth

__all__ = [
    'GetJiraUserAction'
]

class GetJiraUserAction(BaseJiraAction):
	def run(self, accountId):
		user = self._client.get_users(accountId)
		return user

		
