class EmailFormatError(Exception):
    def __str__(self):
        return "Please enter a valid email address."


def is_valid_email(email):
    try:
        username, domain = email.split('@')
        if not username[0].isalpha() or not domain.endswith('student.gsu.edu'):
            raise EmailFormatError
        return True
    except ValueError:
        raise EmailFormatError
    except EmailFormatError as e:
        print(e)
        return False

print(is_valid_email("example@student.gsu.edu"))  
print(is_valid_email("123@student.gsu.edu"))  
