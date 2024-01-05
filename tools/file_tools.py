from langchain.tools import tool

class FileTools():

    @tool("Escrever arquivo com conteúdo")
    def write_file(data):
        """Útil para escrever um arquivo em um caminho específico com um conteúdo dado. 
           A entrada para esta ferramenta deve ser um texto separado por pipe (|) 
           de comprimento dois, representando o caminho completo do arquivo, 
           incluindo o /workdir/template, e o conteúdo do código do Componente React 
           que você deseja escrever nele.
           Por exemplo, `./Keynote/src/components/Hero.jsx|CODIGO_DO_COMPONENTE_REACT`.
           Substitua CODIGO_DO_COMPONENTE_REACT pelo código real 
           que você deseja escrever no arquivo."""
        try:
            path, content = data.split("|")
            path = path.replace("\n", "").replace(" ", "").replace("`", "")
            if not path.startswith("./workdir"):
                path = f"./workdir/{path}"
            with open(path, "w") as f:
                f.write(content)
            return f"Arquivo escrito em {path}."
        except Exception:
            return "Erro no formato de entrada para a ferramenta."
