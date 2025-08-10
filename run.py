from app.main import create_application

# Starts Flask developepment server with run()
if __name__ == '__main__':
    app = create_application()
    app.run(host='0.0.0.0', port=5000, debug=True)
