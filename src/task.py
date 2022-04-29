import os

from task_interfaces import FormatTask, SubscriptionLevels


class Task(TaskInterface):
    """
    Ensure all Terraform files are formatted correctly
    """

    name = "Terraform Format"
    subscription_level = SubscriptionLevels.STARTUP
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)