from factorial import factorial
from httpx import requests



def testHealth():
  response = requests.get('/health')
  
  print(response)
  assert response.status_code == 200
  assert response.json() == {"status": "OK"}