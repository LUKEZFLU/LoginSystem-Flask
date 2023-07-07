# July 7 2023

from website.template._init_ import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True) # Run the flask application

