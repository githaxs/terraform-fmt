import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


class Task(TaskInterface):
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
    type = TaskTypes.CODE_FORMAT
    command = "terraform fmt -no-color -list=false"
    file_filters = ".*.(tf|tfvars)$"

    def execute(self, github_body, settings) -> bool:
        pass
