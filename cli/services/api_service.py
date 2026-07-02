import requests

class ApiService:
    # BASE_URL = "http://127.0.0.1:8000/"
    BASE_URL = "https://fastapi-cli-book-task-production.up.railway.app "
    def get(self, endpoint, params=None):
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()
        
    def post(self, endpoint, data):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=data, timeout=10)
        response.raise_for_status()
        return response.json()
        
    def delete(self, endpoint):
        response = requests.delete(f"{self.BASE_URL}{endpoint}", timeout=10)
        if response.status_code != 204:
            return response.json()
        return None