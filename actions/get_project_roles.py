from lib.base import BaseJiraAction
#from lib.formatters import to_issue_dict

__all__ = [
    'GetJiraProjectRolesAction'
]


class GetJiraProjectRolesAction(BaseJiraAction):
    def run(self, project_key):
        project = self._client.project_roles(project_key)
	print(project)
	#return project
        #result = to_issue_dict(project)
        #return result





