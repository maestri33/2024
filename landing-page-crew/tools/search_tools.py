import os
import json
import requests
from langchain.tools import tool

class SearchTools():

    @tool("Pesquisar na internet")
    def search_internet(query):
        """Útil para pesquisar na internet sobre um determinado tópico 
        e retornar resultados relevantes."""
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']
        string = []
        for result in results:
            string.append('\n'.join([
                f"Título: {result['title']}", f"Link: {result['link']}",
                f"Trecho: {result['snippet']}", "\n-----------------"
            ]))

        return '\n'.join(string)
