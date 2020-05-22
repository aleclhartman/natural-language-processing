import re

def is_vowel(string):
    if re.search(r"[aeiouAEIOU]", string) == None:
        return False
    elif type(re.search(r"[aeiouAEIOU]", string)) == re.Match:
        return True

def is_valid_username(string):
    if re.search(r"^[a-z][a-z0-9]{1,31}$", string) == None:
        return False
    elif type(re.search(r"^[a-z][a-z0-9]{1,31}$", string)) == re.Match:
        return True



def standardize_date(date):
    return re.sub(r"(\d{2})/(\d{2})/(\d{2})", "20" + r"\3-\1-\2", date)