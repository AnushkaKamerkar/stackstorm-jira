 
from lib.base import BaseJiraAction
#from lib.formatters import to_issue_dict

__all__ = [
    'GetJiraUsersAction'
]


class GetJiraUsersAction(BaseJiraAction):
	def run(self, user_id):
		users = self._client.user(user_id)
		print(users)	

		return users
