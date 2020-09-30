from flaskr import create_app


if __name__ == '__main__':
    my_app = lambda x: x()
    my_app(create_app).run(debug=True)

    

