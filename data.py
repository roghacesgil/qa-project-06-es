headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
    "name": "Mi conjunto"
}

one_letter = {
    "name": "a"
}

character_limit = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabC"
}

zero_character = {
    "name": ""
}

character_over_limit = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcD"
}

special_characters = {
    "name": "№%@"
}

spaces_in_name = {
    "name": " A Aaa"
}

numbers_in_name = {
    "name": "123"
}

numbers_instead_of_string = {
    "name": 123
}


# Función para actualizar el token
def update_token(token):
    headers_token = headers.copy()
    headers_token["Authorization"] = f"Bearer {token}"
    return headers_token
