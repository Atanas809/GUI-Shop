import re


def valid_password(password, confirm_password):
    if password == confirm_password:
        if len(password) < 6 or len(password) > 16:
            return False

        return True


def matching_password(password, confirm_password):
    if password != confirm_password:
        return False

    return True


def valid_email(email):
    expression = r"(?P<valid>(^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$))"

    matches = re.finditer(expression, email)

    for match in matches:
        return True
    else:
        return False


