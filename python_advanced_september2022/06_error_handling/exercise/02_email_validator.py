class NameTooShortError(Exception):
    """
    Username is less than or equal to 4 characters.
    """
    pass


class MustContainAtSymbolError(Exception):
    """
    The email must contain "@".
    """
    pass


class InvalidDomainError(Exception):
    """
    Valid domains: .com, .bg, .net, .org
    """
    pass


class MoreThanOneAtSymbolError(Exception):
    """
    The email must contain only one symbol '@'
    """
    pass


def valid_domain(domain_, valid_domains_):
    """
    The function checks if the domain is valid.
    :param domain_: Current domain that needs to be checked.
    :param valid_domains_: List of all valid domains.
    :return: True/False depending on the result from the for loop.
    """
    valid = False
    for dom in valid_domains_:
        if domain_.endswith(dom):
            valid = True
            break
    return valid


valid_domains = ['.com', '.bg', '.org', '.net']

while True:
    current_email = input()
    if current_email == 'End':
        break
    elif '@' not in current_email:
        raise MustContainAtSymbolError("Email must contain @")
    elif current_email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one '@' symbol")

    username, domain = current_email.split("@")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif not valid_domain(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')