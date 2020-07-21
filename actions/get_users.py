 
from lib.base import BaseJiraAction
#from lib.formatters import to_issue_dict

__all__ = [
    'GetJiraUsersAction'
]


class GetJiraUsersAction(BaseJiraAction):
	def run(self, accountId):
		users = self._client.user(accountId)
		print(users)	

		return users
