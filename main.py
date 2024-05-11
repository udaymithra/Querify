from Website import create_app
from utils import time_ago

app=create_app()

app.jinja_env.filters['time_ago'] = time_ago
if __name__ == '__main__':
    print("starting the app")
    app.run(debug=True)

    