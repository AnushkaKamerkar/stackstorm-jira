from lib.base import BaseJiraAction
from requests.auth import HTTPBasicAuth

__all__ = [
    'GetJiraUserAction'
]

class GetJiraUserAction(BaseJiraAction):
	def run(self, accountId):
		user = self.get_users(accountId)
		return user

		
