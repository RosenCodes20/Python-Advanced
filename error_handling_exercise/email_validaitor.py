import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooMuchAtSigns(Exception):
    pass


class TooMuchValidDomains(Exception):
    pass


class NameTooLong(Exception):
    pass


class NotAllowedSymbols(Exception):
    pass


email = input()

MIN_LENGTH_OF_THE_NAME = 4

MAX_LENGTH_OF_THE_NAME = 12

valid_domains = ["com", "bg", "org", "net"]

names = r"[A-Za-z]+"

while email != "End":
    if len(email.split("@")[0]) < MIN_LENGTH_OF_THE_NAME:
        raise NameTooShortError("Your name is too short. It must be 4 characters!")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    if email.split(".")[1] not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following ones: {', '.join('.' + el for el in valid_domains)}")

    if email.count("@") > 1:
        raise TooMuchAtSigns("There are too much @!")

    for element in valid_domains:
        if element in email:
            if email.count(element) > 1:
                raise TooMuchValidDomains("There should be one domain!")

    if len(email.split("@")[0]) >= MAX_LENGTH_OF_THE_NAME:
        raise NameTooLong("The name is too long it must be under 12 letters!")

    if re.findall(names, email.split("@")[0])[0] != email.split("@")[0]:
        raise NotAllowedSymbols("The name must contain only letters, digits and underscores!")

    print("This email is valid!")

    email = input()