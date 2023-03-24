import requests
from assertpy import assert_that

import json
from demo6_api import read_utils


class TestPetShop:
    BASE_URL = "https://petstore.swagger.io/v2"

    def test_add_pet_to_store(self):
        resource = "/pet"
        json_body = read_utils.get_json_from_file("../test_data/add_pet.json")
        headers_data = {
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        response = requests.post(TestPetShop.BASE_URL + resource, headers=headers_data, json=json_body)
        assert_that(200).is_equal_to(response.status_code)

    def test_add_pet_to_store_data(self):
        resource = "/pet"
        json_body = read_utils.get_json_from_file("../test_data/add_pet.json")
        headers_data = {
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        response = requests.post(TestPetShop.BASE_URL + resource, headers=headers_data, json=json_body)
        assert_that(200).is_equal_to(response.status_code)
        assert_that('doggie-6101').is_equal_to(response.json()['name'])

    def test_update_pet_to_store_data(self):
        resource = "/pet"
        json_body = read_utils.get_json_from_file("../test_data/update_pet.json")
        headers_data = {
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        response = requests.put(TestPetShop.BASE_URL + resource, headers=headers_data, json=json_body)
        assert_that(200).is_equal_to(response.status_code)
        assert_that('doggie-kim').is_equal_to(response.json()['name'])

    def test_delete_valid_pet(self):
        pet_id = 610
        resource = f"/pet/{pet_id}"
        head = {"api_key": "pet3245"}
        response= requests.delete(TestPetShop.BASE_URL + resource,headers=head)
        assert_that(200).is_equal_to(response.status_code)

    def test_delete_invalid_pet(self):
        pet_id = 610
        resource = f"/pet/{pet_id}"
        head = {"api_key": "pet3245"}
        response= requests.delete(TestPetShop.BASE_URL + resource,headers=head)
        assert_that(404).is_equal_to(response.status_code)
        # print(response.json())
        # assert_that("Pet not found").is_equal_to()

    def test_demo_auth(self):
        resource="/store/order/101"
        response=requests.get(TestPetShop.BASE_URL+resource)
        token=response.json()['shipDate']

        pet_id = 610
        resource = f"/pet/{pet_id}"
        head = {"Authorization": f"Bearer {token}"}
        response = requests.delete(TestPetShop.BASE_URL + resource, headers=head)
        assert_that(404).is_equal_to(response.status_code)