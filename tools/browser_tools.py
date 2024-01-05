import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

class BrowserTools():

  @tool("Extrair e resumir conteúdo de websites")
  def scrape_and_summarize_kwebsite(website):
    """Útil para extrair e resumir o conteúdo de um website"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Particionando e processando o conteúdo HTML
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content_chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    
    summaries = []
    for chunk in content_chunks:
      agent = Agent(
          role='Pesquisador Principal',
          goal='Realizar pesquisas e resumos incríveis baseados no conteúdo com o qual está trabalhando',
          backstory="Você é um Pesquisador Principal em uma grande empresa e precisa fazer uma pesquisa sobre um determinado tópico.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=f'Analise e resuma o conteúdo abaixo, certifique-se de incluir as informações mais relevantes no resumo, retorne apenas o resumo, nada mais.\n\nCONTEÚDO\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)
