from lib.base import BaseJiraAction
#from lib.formatters import to_project_dict


__all__ = [
    'GetJiraProjectRolesAction'
]


class GetJiraProjectRolesAction(BaseJiraAction):
	def run(self, project_key):
		results=[]
		projects = self._client.project_roles(project_key)

		for role, info in projects.items():
    			results.append(info)
		return results

		




