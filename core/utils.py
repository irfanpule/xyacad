from django.forms.models import model_to_dict
from django.contrib.admin.models import DELETION, ADDITION, CHANGE, LogEntry
from django.contrib.contenttypes.models import ContentType


def get_content_type_for_model(obj):
    return ContentType.objects.get_for_model(obj, for_concrete_model=False)


class Logger:
    """
    beberapa method dibawah ini terinspirasi dari class ModelAdmin
    django.contrib.admin.options
    """
    def model_to_dict_str(self, obj):
        return str(model_to_dict(obj))

    def addition(self, request, obj, message=""):
        message = f"{message} | {self.model_to_dict_str(obj)}"

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(obj).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=ADDITION,
            change_message=message,
        )

    def change(self, request, obj, message=""):
        message = f"{message} | {self.model_to_dict_str(obj)}"

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(obj).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=CHANGE,
            change_message=message,
        )

    def deletion(self, request, obj, message=""):
        message = f"{message} | {self.model_to_dict_str(obj)}"

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(obj).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=DELETION,
            change_message=message
        )
