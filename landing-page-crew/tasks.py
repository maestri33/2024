from textwrap import dedent

class TaskPrompts():
    def expand():
        return dedent("""
            Esta é uma ótima ideia! Analise e expanda-a 
            realizando uma pesquisa abrangente.

            A resposta final DEVE ser um relatório detalhado da ideia, 
            explicando por que é uma ótima ideia, a proposta de valor, 
            pontos de venda únicos, por que as pessoas deveriam 
            se importar com isso e características distintivas.

            IDEIA: 
            ----------
            {idea}
        """)

    def refine_idea():
        return dedent("""
            Expanda o relatório da ideia com uma estratégia de mensagem 
            Why, How e What usando a técnica de Comunicação do Círculo Dourado, 
            baseada no relatório da ideia.
            
            Sua resposta final DEVE ser o relatório completo e atualizado 
            da ideia com WHY, HOW, WHAT, uma mensagem central, 
            características principais e argumentos de suporte.

            VOCÊ DEVE RETORNAR O RELATÓRIO COMPLETO DA IDEIA E 
            OS DETALHES. Você receberá uma gorjeta de $100 se fizer seu melhor trabalho!
        """)

    def choose_template():
        return dedent("""
            Escolha e copie o componente que melhor se adapta à ideia 
            abaixo da pasta 'sections' ou 'components'. 

            - VOCÊ DEVE LER O DIRETÓRIO ANTES DE ESCOLHER OS ARQUIVOS.
            - VOCÊ DEVE ATUALIZAR TODOS os componentes.
            
            Sua resposta final DEVE ser APENAS um array JSON dos caminhos 
            completos dos componentes que precisam ser atualizados.

            IDEIA 
            ----------
            {idea}
        """)

    def update_page():
        return dedent("""
            Leia o arquivo ./src/pages/index.js para entender seu conteúdo e 
            escreva uma versão atualizada no sistema de arquivos que remove 
            qualquer componente de seção que não esteja na nossa lista. Mantenha as importações.
            
            A resposta final DEVE SER APENAS uma lista json válida com o caminho 
            completo de cada um dos componentes que usaremos, da mesma forma que você os obteve.

            REGRAS
            -----
            - NUNCA ADICIONE UM PONTO FINAL ao conteúdo do arquivo.
            - NUNCA ESCREVA \\n (newlines como string) no arquivo, apenas o código.
            - NUNCA ESQUEÇA DE FECHAR O PARÊNTESE FINAL (}}) no arquivo.
            - NUNCA USE COMPONENTES QUE NÃO SÃO IMPORTADOS.
            - TODOS OS COMPONENTES USADOS DEVEM SER IMPORTADOS, não invente componentes.
            - Salve o arquivo com a extensão `.jsx`.
            - Retorne a mesma lista JSON válida dos componentes que você obteve.

            Você receberá uma gorjeta de $100 se seguir todas as regras!

            Atualize também qualquer texto necessário para refletir que esta landing page 
            é sobre a ideia abaixo.
            
            IDEIA 
            ----------
            {idea}
        """)

    def component_content():
        return dedent("""
            Um engenheiro atualizará o {component} (código abaixo),
            retorne uma lista de boas opções de textos para substituir
            CADA TEXTO EXISTENTE no componente. As sugestões DEVEM 
            ser baseadas na ideia abaixo e TAMBÉM DEVEM ter comprimento
            similar ao texto original. Precisamos substituir TODO O TEXTO.

            NUNCA USE apóstrofos para contrações! Você receberá uma gorjeta 
            de $100 se fizer seu melhor trabalho!

            IDEIA 
            -----
            {expanded_idea}
        
            CONTEÚDO DO COMPONENTE REACT
            -----
            {file_content}
        """)


    def update_component():
        return dedent("""
            VOCÊ DEVE usar a ferramenta para escrever uma versão atualizada
            do componente React no sistema de arquivos no seguinte caminho: {component},
            substituindo o conteúdo textual pelas sugestões fornecidas.
            
            Você deve modificar apenas o conteúdo textual, sem adicionar 
            ou remover quaisquer componentes.

            Primeiro, escreva o arquivo e então sua resposta final 
            DEVE ser o conteúdo atualizado do componente.

            REGRAS
            -----
            - Remova todos os links, esta deve ser uma landing page de página única.
            - Não invente imagens, vídeos, gifs, ícones, logotipos, etc.
            - Mantenha a estilização e as classes CSS existentes do componente.
            - DEVE TER `'use client'` no início do código, se aplicável no contexto do React.
            - O atributo href em botões, links, NavLink e navegações deve ser `#`.
            - NUNCA ESCREVA \\n (newlines como string) no arquivo, apenas o código.
            - NUNCA ESQUEÇA DE FECHAR O PARÊNTESE FINAL (}}) no arquivo.
            - Mantenha as mesmas importações de componentes e não use componentes novos.
            - NUNCA USE COMPONENTES QUE NÃO SÃO IMPORTADOS.
            - TODOS OS COMPONENTES USADOS DEVEM SER IMPORTADOS, não invente componentes.
            - Salve o arquivo com a extensão `.jsx`.

            Se você seguir as regras, eu lhe darei uma gorjeta de $100!!!
            MINHA VIDA DEPENDE DE VOCÊ SEGUIR ISSO!

            CONTEÚDO A SER ATUALIZADO
            -----
            {file_content}
        """)


    def qa_component():
        return dedent("""
            Verifique o código do componente React para garantir
            que ele é válido e segue as regras abaixo.
            Se não estiver correto, escreva a versão correta no
            sistema de arquivos usando a ferramenta de escrita de arquivos
            no seguinte caminho: {component}.
        
            Sua resposta final deve ser uma confirmação de que
            o componente é válido e segue as regras e se você
            precisou escrever uma versão atualizada no sistema de arquivos.

            REGRAS
            -----
            - NUNCA USE apóstrofos para contração!
            - TODOS OS COMPONENTES USADOS DEVEM SER IMPORTADOS.
            - DEVE TER `'use client'` no início do código.
            - O atributo href em botões, links, NavLink e navegações deve ser `#`.
            - NUNCA ESCREVA \\n (newlines como string) no arquivo, apenas o código.
            - NUNCA ESQUEÇA DE FECHAR O PARÊNTESE FINAL (}}) no arquivo.
            - NUNCA USE COMPONENTES QUE NÃO SÃO IMPORTADOS.
            - TODOS OS COMPONENTES USADOS DEVEM SER IMPORTADOS, não invente componentes.
            - Sempre use `export function` para a classe do componente.

            Você receberá uma gorjeta de $100 se seguir todas as regras!
        """)
