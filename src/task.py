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
    _actions = [
        {
            "label": "Fix",
            "identifier": "fix",
            "description": "Fix formatting issues."
        }
    ]

    def execute(self, github_body, settings) -> bool:

        fix_options = {
            'enabled': False,
            'message': 'style: formatting code with %s' % self.name
        }

        head_branch = None
        base_branch = None

        # A request to fix formatting has been made
        if (
            github_body.get("githaxs", {}).get("full_event")
            == "check_run.requested_action"
            and github_body.get("requested_action", {}).get("identifier", "")
            == "fix"
        ):
            fix_options['enabled'] = True
            head_branch = github_body['check_run']['pull_requests'][0]['head']['ref']
            base_branch = github_body['check_run']['pull_requests'][0]['base']['ref']

        else:
            head_branch = github_body['pull_request']['head']['ref']
            base_branch = github_body['repository']['default_branch']

        subscription_includes_autofix = github_body.get('githaxs').get('subscription_level') >= SubscriptionLevels.GROWTH

        if subscription_includes_autofix and settings.get('auto_fix') == True:
            fix_options['enabled'] = True

        code_check = CodeCheck(
            token=github_body.get('githaxs').get('token'),
            branch = head_branch,
            default_branch = base_branch,
            full_repo_name = github_body.get('repository', {}).get('full_name'),
            source_script_path = '%s/task.sh' % os.path.dirname(__file__),
            fix_options=fix_options

        )

        code_check.execute()

        self.fail_text = code_check.fail_text

        # If check passed, no extra actions needed
        if code_check.result:
            self._actions = None

        return code_check.result

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, actions):
        self._actions = actions