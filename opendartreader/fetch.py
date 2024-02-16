import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get(url, params={}, stream=False, headers={}):
    # url = 'https://opendart.fss.or.kr/api/company.json?crtfc_key=f70a67370062b2c2e125bb708241b0b7f354175d&corp_code=00126380'

    # Use Session and Disable the SSL Cert Check
    session = requests.Session()
    session.verify = False
    session.trust_env = False
    response = session.get(url, params=params, stream=stream, headers=headers)
    # response.text
    return response