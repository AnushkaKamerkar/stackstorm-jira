from lib.base import BaseJiraAction
from lib.formatters import to_project_dict

__all__ = [
    'GetJiraProjectComponentsAction'
]


class GetJiraProjectComponentsAction(BaseJiraAction):
	def run(self, project_key):
		projects = self._client.project_components(project_key)
		print(projects)
		results = []
		for project_key in projects:
				results.append(to_project_dict(project_key=project_key))				
		return results


