import re

def extract_family_name(name: str) -> str:
    """Given a name, extract the family name

    Parameters
    ----------
    name : str
        The full name text (e.g. The Roberts Family,
        Mr. and Mrs. Smith)

    Returns
    -------
    str
        The family name (e.g. Smith)
    """
    
    regex_words = re.compile('[a-zA-Z]+')
    name_words = regex_words.findall(name)
    no_family = [word for word in name_words if word not in ['Family', 'and']]
    family_name = no_family[-1]
    return family_name