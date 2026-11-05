import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    if name is not None:
        current_body["name"] = name
    else:
        current_body.pop("name", None)
    return current_body


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json().get("authToken")


def positive_assert(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Prueba 1: El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# Prueba 2: El número permitido de caracteres (511)
def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)


# Prueba 5: Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)


# Prueba 6: Se permiten espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# Prueba 7: Se permiten números
def test_create_kit_has_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# Prueba 8: El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = get_kit_body(None)
    negative_assert_code_400(kit_body)


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_different_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)