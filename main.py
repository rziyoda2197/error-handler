class ErrorHandler:
    def __init__(self):
        self.error_codes = {
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error"
        }

    def handle_error(self, error_code):
        if error_code in self.error_codes:
            return self.error_codes[error_code]
        else:
            return "Unknown Error"

    def handle_exception(self, exception):
        error_code = getattr(exception, 'code', 500)
        return self.handle_error(error_code)

def main():
    error_handler = ErrorHandler()

    try:
        # Simulate an error
        raise Exception('Test Error', code=404)
    except Exception as e:
        print(error_handler.handle_exception(e))

if __name__ == "__main__":
    main()
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Kodni yuklab oling va Python ni o'rnatgan kompyuterda ishlab ko'ring.
2. Kodni yuklab oling va ishlab ko'ring.
3. Simulyatsiya qilingan xatoning uchun 404 kodini kiritib ko'ring.
4. Natijani ko'ring.
