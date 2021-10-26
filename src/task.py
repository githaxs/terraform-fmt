import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


class Task(TaskInterface):
    """
    Ensure all Terraform files are formatted correctly
    """

    name = "Terraform Format"
    slug = "terraform-format"
    pass_summary = ""
    pass_text = ""
    fail_summary = "Files not formatted correctly."
    fail_text = ""
    subscription_level = SubscriptionLevels.FREE

    actions = None
    can_fix = True

    type = TaskTypes.CODE_FORMAT
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
    handler = "task"

    def execute(self, github_body, settings) -> bool:
        pass
