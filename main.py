# July 7 2023
# Using this file to open and run the app

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True) # Run the flask application

