import json
import os
import shutil
from textwrap import dedent

from crewai import Agent, Crew, Task
from langchain.agents.agent_toolkits import FileManagementToolkit
from tasks import TaskPrompts

from tools.browser_tools import BrowserTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools
from tools.template_tools import TemplateTools

from dotenv import load_dotenv
load_dotenv()

class LandingPageCrew():
  def __init__(self, idea):
    self.agents_config = json.loads(open("config/agents.json", "r").read())
    self.idea = idea
    self.__create_agents()

  def run(self):
    expanded_idea = self.__expand_idea()
    components = self.__choose_template(expanded_idea)
    self.__update_components(components, expanded_idea)

  def __expand_idea(self):
    expand_idea_task = Task(
      description=TaskPrompts.expand().format(idea=self.idea),
      agent=self.idea_analyst
    )
    refine_idea_task = Task(
      description=TaskPrompts.refine_idea(),
      agent=self.communications_strategist
    )
    crew = Crew(
      agents=[self.idea_analyst, self.communications_strategist],
      tasks=[expand_idea_task, refine_idea_task],
      verbose=True
    )
    expanded_idea = crew.kickoff()
    return expanded_idea

  def __choose_template(self, expanded_idea):
    choose_tempalte_taks = Task(
        description=TaskPrompts.choose_template().format(
          idea=self.idea
        ),
        agent=self.react_developer
    )
    update_page = Task(
      description=TaskPrompts.update_page().format(
        idea=self.idea
      ),
      agent=self.react_developer
    )
    crew = Crew(
      agents=[self.react_developer],
      tasks=[choose_tempalte_taks, update_page],
      verbose=True
    )
    components = crew.kickoff()
    return components

  def __update_components(self, components, expanded_idea):
    components = components.replace("\n", "").replace(" ",
                                                      "").replace("```", "")
    components = json.loads(components)
    for component in components:
      file_content = open(
        f"./workdir/{component.split('./')[-1]}",
        "r"
      ).read()
      create_content = Task(
        description=TaskPrompts.component_content().format(
          expanded_idea=expanded_idea,
          file_content=file_content,
          component=component
        ),
        agent=self.content_editor_agent
      )
      update_component = Task(
        description=TaskPrompts.update_component().format(
          component=component,
          file_content=file_content
        ),
        agent=self.react_developer
      )
      qa_component = Task(
        description=TaskPrompts.qa_component().format(
          component=component
        ),
        agent=self.react_developer
      )
      crew = Crew(
        agents=[self.content_editor_agent, self.react_developer],
        tasks=[create_content, update_component, qa_component],
        verbose=True
      )
      crew.kickoff()

  def __create_agents(self):
    idea_analyst_config = self.agents_config["senior_idea_analyst"]
    strategist_config = self.agents_config["senior_strategist"]
    developer_config = self.agents_config["senior_react_engineer"]
    editor_config = self.agents_config["senior_content_editor"]

    toolkit = FileManagementToolkit(
      root_dir='workdir',
      selected_tools=["read_file", "list_directory"]
    )

    self.idea_analyst = Agent(
      **idea_analyst_config,
      verbose=True,
      tools=[
        SearchTools.search_internet,
        BrowserTools.scrape_and_summarize_kwebsite
      ]
    )

    self.communications_strategist = Agent(
      **strategist_config,
      verbose=True,
      tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_kwebsite,
      ]
    )

    self.react_developer = Agent(
      **developer_config,
      verbose=True,
      tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_kwebsite,
          TemplateTools.learn_landing_page_options,
          TemplateTools.copy_landing_page_template_to_project_folder,
          FileTools.write_file
      ] + toolkit.get_tools()
    )

    self.content_editor_agent = Agent(
      **editor_config,
      tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_kwebsite,
      ]
    )
def carregar_ideia(arquivo_ideia):
    with open(arquivo_ideia, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Ideias")
    print(dedent("""
    ! VOCÊ DEVE FORKAR ESTE PROJETO ANTES DE USÁ-LO !
    """))

    print(dedent("""
        Aviso: Isso usará gpt-4 a menos que você o altere,
        e isso custará dinheiro (aproximadamente 2-9 USD).
        A execução completa pode levar cerca de 10-45 minutos. Aproveite seu tempo livre.\n\n
    """))
    
    caminho_arquivo_ideia = "idea.txt"
idea = carregar_ideia(caminho_arquivo_ideia)

if not os.path.exists("./workdir"):
        os.mkdir("./workdir")

    # Adaptando para verificar a existência de componentes no novo template
if not os.path.exists("./src/components") or not os.listdir("./src/components"):
        print(dedent("""
            !!! NENHUM COMPONENTE ENCONTRADO !!!
            Certifique-se de que os componentes do React estão disponíveis em './src/components'.
            
            A execução será interrompida.
            """))
        exit()

crew = LandingPageCrew(idea)
crew.run()
zip_file = "workdir"
shutil.make_archive(zip_file, 'zip', 'workdir')
shutil.rmtree('workdir')
print("\n\n")
print("==========================================")
print("CONCLUÍDO!")
print("Você pode baixar o projeto em ./{zip_file}.zip")
print("==========================================")