from lib.base import BaseJiraAction

__all__ = [
    'GetJiraIssueChangeLogAction'
]

issue/{issueIdOrKey}/changelog

class GetJiraIssueChangeLogAction(BaseJiraAction):
	def run(self, issue_key, start_at=0, max_results=50):
		issue = self._client.find("issue/{issueIdOrKey}/changelog", issue_key)
		print(issue)
		return issue
	





