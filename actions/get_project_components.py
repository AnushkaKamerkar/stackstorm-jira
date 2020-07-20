from lib.base import BaseJiraAction
#from lib.formatters import to_issue_dict

__all__ = [
    'GetJiraProjectComponentsAction'
]


class GetJiraProjectComponentsAction(BaseJiraAction):
	def run(self, project_key):
		project = self._client.project_components(project_key)
		print(project)
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
		return project
		#result = to_issue_dict(project)
		#return result
