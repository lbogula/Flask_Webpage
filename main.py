from website import create_app #website folder is a python package because of the init file

app = create_app()

if __name__ == '__main__': # app runs only if executed, otherwise it would already start upon import of the package
    app.run(debug=True)