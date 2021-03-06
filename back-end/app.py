from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# Configuration
DEBUG = True

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

books = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# Sanity Check Route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        books.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book Added!'
    else:
        response_object['books'] = books

    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        
        book_list_idx = None
        for idx, book in enumerate(books):
            if book["id"] == book_id:
                book_list_idx = idx
                break

        if book_list_idx is not None:
            books[book_list_idx]['title'] = post_data.get('title')
            books[book_list_idx]['author'] = post_data.get('author')
            books[book_list_idx]['read'] = post_data.get('read')

            response_object['message'] = 'Book updated!'
        else:
            response_object['message'] = 'Book could not be found in order to be updated...'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def remove_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return True
    return False


if __name__ == '__main__':
    app.run()
