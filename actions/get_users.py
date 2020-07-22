from lib.base import BaseJiraAction

__all__ = [
    'GetJiraUserAction'
]


class GetJiraUserAction(BaseJiraAction):
	def run(self, group):
		group = self._client.group_members("jira-users")
		for users in group:
		    print users

		return group
