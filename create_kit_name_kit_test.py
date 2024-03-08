import sender_stand_request
import data


# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(kit_body):
    current_name = data.kit_body.copy()
    current_name["name"] = kit_body
    return current_name


# Función de prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    kit_response_data = kit_response.json()
    assert kit_response.status_code == 201
    assert kit_response_data["name"] == kit_body["name"]


# Función de prueba negativa
def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# Prueba 1: Número de caracteres permitido(1)
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert(data.one_letter)


def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert(data.character_limit)


def test_create_kit_empty_character_in_name_get_error_response():
    negative_assert_symbol(data.zero_character)


def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_symbol(data.character_over_limit)


def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(data.special_characters)


def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(data.spaces_in_name)


def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(data.numbers_in_name)


def test_create_kit_no_name_get_error_response():
    current_body_kit = data.kit_body.copy()
    negative_assert_no_name(current_body_kit)


def test_create_kit_different_type_of_data_get_error_response():
    negative_assert_symbol(data.numbers_instead_of_string)
