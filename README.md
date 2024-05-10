This repository is my exam paper, I make back-end testing for the API Simple-books-api in Phycharm.
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md -link to the Simple books API


I found 3 bugs:

1.      This bug is the same for 2 tests:
   
a.      def test_patch_order_flow(self):
        book_id = 1
        customer_name = "Jane Doe"
        order_id = self.books.post_books_order(self.accessToken, book_id, customer_name).json()['orderId']
        customer_name = "Susan"
        response = self.books.pach_books_order(self.accessToken, order_id, customer_name)
        assert response.status_code == 201, "PATCH/orders/{id} status code it is not the same "
        
        Expected :201
        Actual   :204

        Steps to reproduce:
        -it is necessary to create a token in Postman
        -it is necessary to create a book with POST 
        - PACH the book we created, changing the customerName
        The expected result must be, to inform the client that  requested changes was made successfully status code 201.
        Actual result is 204, No Content.

  b.        def test_delete_book_order(self):
        book_id = 5
        customer_name = "John"
        order_id = self.books.post_books_order(self.accessToken, book_id, customer_name).json()['orderId']
        response = self.books.delete_books_order(self.accessToken, order_id)
        assert response.status_code == 201, "status code is not te same "

        Expected :201
        Actual   :204

         Steps to reproduce:
        -it is necessary to create a token in Postman
        -it is necessary to create a book with POST 
        - PACH the book we created, changing the customerName
        - DELETE the book we created
        The expected result must be, to inform the client that  the DELETE request was made successfully status code 201.
        Actual result is 204, No Content.




3.      def test_books_by_filter_invalid_limit_string(self):
        limit = "abc"
        book_type = ""
        response = self.books.get_api_books_by_filter(limit, book_type)
        assert response.status_code == 400, "status code is not the same "   

    Expected :400
    Actual   :200
 
    The expected result is 400 bad request, "eroor":"invalid value for query parameter"
    Actual result in the Postman shows a status code of 200 and a list of all the books. The limit is numeric .

       
        

