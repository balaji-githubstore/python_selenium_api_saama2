import requests
from assertpy import assert_that


class TestPetShop:
    END_POINT = "https://petstore.swagger.io/v2"

    """Get request for path parameter. Validating status code and data present """
    """ Positive response """

    def test_get_pet_by_id(self):
        pet_id = 610
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetShop.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)
        # assert_that("doggie").contains(response.json()['name'])

    """ Negative response """

    def test_get_not_avaiable_pet_by_id(self):
        pet_id = 610
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetShop.END_POINT + resource)
        assert_that(404).is_equal_to(response.status_code)
        print(response.json())
        assert_that("Pet not found").contains(response.json()['message'])

    """ Printing data from response """

    def test_get_pet_by_id_print(self):
        pet_id = 610
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetShop.END_POINT + resource)
        print(response)
        print(response.status_code)
        print(response.json())
        print(response.json()['id'])
        # print(response.json()['name'])
        # print(response.json()['category'])
        # print(response.json()['category']['id'])
        # print(response.json()['category']['name'])

    """Get request for query parameter. Validating status code and data present """
    """ Positive response """

    def test_get_pet_by_status(self):
        resource = "/pet/findByStatus?status=sold"
        response = requests.get(TestPetShop.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)

    """ Negative response """
    def test_get_pet_by_wrong_status(self):
        resource = "/pet/findByStatus?status=sold1223"
        response = requests.get(TestPetShop.END_POINT + resource)
        assert_that(400).is_equal_to(response.status_code)

    """ Printing data from response """

    def test_get_pet_by_status_print(self):
        resource = "/pet/findByStatus?status=sold"
        response = requests.get(TestPetShop.END_POINT + resource)
        print(response.json())  # list of dic
        print(response.json()[0])
        print(response.json()[0]['id'])
        # print(response.json()[0]['name'])
        print(response.json()[0]['category'])
        print(response.json()[0]['category']['id'])
        print(response.json()[0]['category']['name'])

    def test_get_pet_id_by_status_print(self):
        resource = "/pet/findByStatus?status=sold"
        response = requests.get(TestPetShop.END_POINT + resource)
        for dic in response.json():
            print(dic['id'])

