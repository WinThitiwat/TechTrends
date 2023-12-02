from app import create_app
import logging
from config import Config

log_format = '%(levelname)s | %(name)s | %(asctime)s | %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=log_format, level=logging.DEBUG, datefmt=date_format)

app = create_app(Config)


if __name__ == '__main__':
    app.run(debug=True, port=3111)
