# from dart import OpenDartReader
from dotenv import load_dotenv
import os

import sys
from os import path
print(path.dirname( path.dirname( path.abspath(__file__) ) ))
sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))

load_dotenv(dotenv_path='./.env',verbose=True)

def main():
    from dart import OpenDartReader
    api_key = os.environ['API_KEY']
    print("API_KEY", api_key)
    dart = OpenDartReader(api_key) 
    print(dart.company('삼성전자'))


if __name__ == "__main__":
    """
        OpenDartReader text
    """

    main()