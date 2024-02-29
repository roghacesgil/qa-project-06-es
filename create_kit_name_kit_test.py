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


# Función de prueba negativa para valores
def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

# Función de prueba negativa al eliminar un campo
def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# Prueba 1: Número de caracteres permitido(1)
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert("a")


# Prueba 2: Número de caracteres permitidos(511)
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabC")


# Prueba 3: Dejar el cuerpo del kit vacío
def test_create_kit_empty_character_in_name_get_error_response():
    current_body_kit = get_kit_body("")
    negative_assert_symbol(current_body_kit)


# Prueba 4: Más números de los permitidos en el nombre(512)
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdAbcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcD")


# Prueba 5: Caracteres especiales en el nombre
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert("№%@")


# Prueba 6: Espacios en el nombre
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")


# Prueba 7: Números en el nombre
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Prueba 8: Eliminar el campo nombre
def test_create_kit_no_name_get_error_response():
    current_body_kit = data.kit_body.copy()
    current_body_kit.pop("name")
    negative_assert_no_name(current_body_kit)


# Prueba 9: Datos numericos en el nombre (no strings)
def test_create_kit_different_type_of_data_get_error_response():
    negative_assert_symbol(123)
