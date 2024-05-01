from Website import create_app


app=create_app()

if __name__ == '__main__':
    print("starting the app")
    app.run(debug=True)

    