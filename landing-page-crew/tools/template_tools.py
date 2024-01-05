import json
import shutil
from pathlib import Path
from langchain.tools import tool

class TemplateTools():

    @tool("Aprender opções de templates de landing page")
    def learn_landing_page_options(input):
        """Aprenda os templates à sua disposição"""
        templates = json.load(open("config/templates.json"))
        return json.dumps(templates, indent=2)

    @tool("Copiar template de landing page para a pasta do projeto")
    def copy_landing_page_template_to_project_folder(landing_page_template):
        """Copia um template de landing page para sua pasta de projeto 
        para que você possa começar a modificá-lo. Espera como entrada 
        a pasta do template de landing page."""
        source_path = Path(f"templates/{landing_page_template}")
        destination_path = Path(f"workdir/{landing_page_template}")
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source_path, destination_path)
        return f"Template copiado para {landing_page_template} e pronto para ser modificado, os arquivos principais devem estar em ./{landing_page_template}/src/components, você deve focar nesses."
