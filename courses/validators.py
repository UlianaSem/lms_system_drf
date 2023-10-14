import re

from rest_framework.exceptions import ValidationError


class NameAndDescriptionValidator:

    reg = r"^(www\.|http:\/\/|https:\/\/).*(\.ru|\.com|\.рф).*"
    youtube = "youtube.com"

    def __call__(self, value):
        if self.youtube not in value:

            if bool(re.match(self.reg, value)):
                raise ValidationError("FORBIDDEN URL")
