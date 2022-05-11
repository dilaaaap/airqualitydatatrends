import pytest, requests

def test_Flask():
	response = requests.get('http://localhost:5000/route')
	assert response.status_code == 200

	response = requests.get('http://localhost:5000/jobs')
