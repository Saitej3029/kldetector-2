import requests

class VirusTotalAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3/"

    def get_url_analysis(self, url):
        headers = {
            'x-apikey': self.api_key
        }
        response = requests.get(self.base_url + 'urls/' + url, headers=headers)
        return response.json()

    def get_file_analysis(self, file_hash):
        headers = {
            'x-apikey': self.api_key
        }
        response = requests.get(self.base_url + 'files/' + file_hash, headers=headers)
        return response.json()