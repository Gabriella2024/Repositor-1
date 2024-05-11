import unittest

from requests_apis.Book_Api import Book_Api


class Test_Books():
    books = Book_Api()
    accessToken = books.post_api_clients().json()['accessToken']

    def test_books_status(self):
        response = self.books.get_api_status_response()
        assert response.status_code == 200, 'Status code is not the same '
        assert response.json()["status"] == "OK", " GET/status response value for key 'status' is not the same: "

    def test_all_books(self):
        response = self.books.get_api_books_response()
        assert response.status_code == 200, "status ode is not te same: "

        expected_number = 6
        assert len(response.json()) >= expected_number, 'GET/books length is not the same: '


    def test_book_by_id(self):
        response = self.books.get_api_book_by_id(1)

        assert response.status_code == 200, "status code is not the same: "
        assert response.json()["id"] == 1
        assert len([response.json()]) == 1


    def test_book_by_id_string(self):
        non_existing_id = "wow"
        response = self.books.get_api_book_by_id(non_existing_id)
        assert response.status_code == 404, "status code is not the same: "
        assert response.json()['error'], f"No book with id NaN"

    def test_book_by_id_negative_number(self):
        negative_id_number = -1
        response = self.books.get_api_book_by_id(negative_id_number)
        assert response.status_code == 404, "status code is not the same: "
        assert response.json()["error"], f"No book with id {negative_id_number}"
        f'GET/books/{id} response value for key \'id\' is not the same '

    def test_book_oders_no_token(self):
        response = self.books.get_api_orders_response('2658745558745')
        assert response.status_code == 401, "status code is not te same "

    def test_post_orders(self):
        book_id = 1
        customer_name = "John Doe"
        token = self.accessToken
        response = self.books.post_books_order(token, book_id, customer_name)
        assert response.status_code == 201, 'status code it is not the same '


    def test_get_all_orders(self):
        response = self.books.get_api_orders_response(self.accessToken)
        assert response.status_code == 200, "status code it is not te same "

    def test_post_order_flow(self):
        book_id = 1
        customer_name = "Jane Doe"
        response = 21
        order_id = self.books.post_books_order(self.accessToken, book_id, customer_name).json()["orderId"]
        assert response == 21, len(order_id)
        "GET/orders length is not the same: "

    def test_patch_order_flow(self):
        book_id = 1
        customer_name = "Jane Doe"
        order_id = self.books.post_books_order(self.accessToken, book_id, customer_name).json()['orderId']

        customer_name = "Susan"
        response = self.books.pach_books_order(self.accessToken, order_id, customer_name)
        assert response.status_code == 201, "PATCH/orders/{id} status code it is not the same "

    def test_books_by_filter_type_and_limit(self):
        limit = 2
        book_type = "fiction"
        response = self.books.get_api_books_by_filter(limit, book_type)
        assert response.status_code == 200, "status code is not the same "
        assert len(response.json()) == 2

    def test_books_by_filter_limit(self):
        limit = 1
        book_type = ""
        response = self.books.get_api_books_by_filter(limit,book_type )
        assert response.status_code == 200, "status code is not the same "



    def test_books_by_filter_type_fiction(self):
        limit = ""
        book_type = "fiction"
        response = self.books.get_api_books_by_filter(limit, book_type)
        book_list = response.json()
        is_type_corect = True
        for i in range(len(book_list)):
            if book_list[i]["type"] != "fiction":
                is_type_corect = False



        assert response.status_code == 200, f"status code is not the same "
        assert is_type_corect == True, "at least one book has an other type"


    def test_books_by_filter_type_non_fiction(self):
        limit = ""
        book_type = "non-fiction"
        response = self.books.get_api_books_by_filter(limit, book_type)
        assert response.status_code == 200, f"status code is not the same "

    def test_books_by_filter_invalid_limit_negative(self):
        limit = -1
        book_type = ""
        response = self.books.get_api_books_by_filter(limit, book_type)
        assert response.status_code == 400, "status code is not the same "

    def test_books_by_filter_invalid_limit_string(self):
        limit = "abc"
        book_type = ""
        response = self.books.get_api_books_by_filter(limit, book_type)
        assert response.status_code == 400, "status code is not the same "

    def test_delete_book_order(self):
        book_id = 5
        customer_name = "John"
        order_id = self.books.post_books_order(self.accessToken, book_id, customer_name).json()['orderId']
        response = self.books.delete_books_order(self.accessToken, order_id)
        assert response.status_code == 201, "status code is not te same "


