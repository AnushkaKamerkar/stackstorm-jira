 
from lib.base import BaseJiraAction
#from lib.formatters import to_issue_dict

__all__ = [
    'GetJiraUsersAction'
]


class GetJiraUsersAction(BaseJiraAction):
	def run(self, user, start_at=0, max_results=50,include_active=True, include_inactive=False):
		users = self._client.search_users(user, startAt=start_at,maxResults=max_results,includeActive=include_active)
		for u in users:
			print(u)	

		return users
