import os

from dotenv import load_dotenv

from manage import main

if __name__ == '__main__':
    os.environ.setdefault('ENVIRONMENT', 'test')
    load_dotenv('../config/.env')
    main()
