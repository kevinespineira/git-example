from app import app

if __name__ == '__main__':
    app.config['VERSION'] = '1.0.0'
    app.run(debug=True)