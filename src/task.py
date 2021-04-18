import os

from task_interfaces import MetaTaskInterface, SubscriptionLevels
from code_check import CodeCheck


class Task(MetaTaskInterface):
    """
    Ensure all Terraform files are formatted correctly
    """

    name = "Terraform Format"
    slug = "terraform-fmt "
    pass_summary = ""
    pass_text = ""
    fail_summary = "Files not formatted correctly."
    fail_text = ""
    subscription_level = SubscriptionLevels.FREE
    actions = None

    def execute(self, github_body, settings) -> bool:
        code_check = CodeCheck(
            token=github_body.get('githaxs').get('token'),
            branch = github_body.get('pull_request', {}).get('head', {}).get('ref'),
            default_branch = github_body.get('repository', {}).get('default_branch'),
            full_repo_name = github_body.get('repository', {}).get('full_name'),
            source_script_path = '%s/task.sh' % os.path.dirname(__file__)

        )

        code_check.execute()

        self.fail_text = code_check.fail_text

        return code_check.result