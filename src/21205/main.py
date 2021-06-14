def check_registration_rules(**kwargs):
    valid_username = []
    for username, password in kwargs.items():
        if (len(username) >= 4) and (username not in ['quera', "codecup"]) and (len(password) >= 6) and (not password.isdigit()):
            valid_username.append(username)
    return valid_username


