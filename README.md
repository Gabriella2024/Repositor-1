This repository is my exam paper, I make back-end testing for the API Simple-books-api in Phycharm.
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md -link to the Simple books API

Prerequisites:

It is necessary to have installed python 3.11 and pip.

python 3.11
Check if you already have Python installed running the Terminal command: python --version. If the result shows a version number, Python is already installed. If not, you can download it 
here: https://www.python.org/downloads/

pip
Check if you have already pip installed running the Terminal command: pip --version. If the result shows a version number, pip is installed and there is no need for further actions. If 
not, instructions for downloading the latest version of pip can be found here: https://pip.pypa.io/en/stable/cli/pip_download/
Pip is the package manager for Python. It is used to install and update packages in a virtual environment.

Running the tests :

After creating the project file in Pycharm, I created the 2 Pyton files, one for the definition of variables, constants and the other one for tests in Python.
![image](https://github.com/Gabriella2024/Repositor-1/assets/167851863/20850ffe-b3c9-4092-8d41-f3c7ad2928d0)

To run any test, found in the tests folder you can run the corresponding file.
![image](https://github.com/Gabriella2024/Repositor-1/assets/167851863/47510065-0fa0-4bf5-bdb3-19a869bc78ef)


To generate the report, run the Terminal command:

pytest --html=report.html


![2](https://github.com/Gabriella2024/Repositor-1/assets/167851863/829c25d3-e298-4614-83c1-fb15fba605dd)



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

       
        

