from app import app

print(f"Nome: {__name__}")


if (__name__ == '__main__'):
    app.run(debug=True)