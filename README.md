<p align="center">
  <img src="./docs/assets/logo-neoenergia.svg" alt="Logo da Neoenergia Brasília" width="250">
</p>

# Processo de Avaliação de Produto de Software

Este repositório contém a documentação do projeto prático da disciplina de Qualidade de Software do curso de Engenharia de Software da Universidade de Brasília (UnB).

## Objeto de Avaliação

O produto de software selecionado pelo grupo para passar pelo processo de avaliação é a **[Agência Virtual da Neoenergia Brasília](https://agenciavirtual.neoenergiabrasilia.com.br/)**.

## Estrutura da Avaliação

O projeto reflete a aplicação prática dividida em quatro fases metodológicas:
1. **Fase 1:** Estabelecer requisitos de avaliação
2. **Fase 2:** Especificar a avaliação
3. **Fase 3:** Projetar a avaliação
4. **Fase 4:** Executar a avaliação (e Conclusão)



## Integrantes do Grupo

- Arthur de Lima Sobreira - 231026797
- Beatriz Figueiredo dos Santos - 232046050
- Dara Maria Barbosa de Sousa - 202046040
- Henrique Martins Alencar - 211061860
- Isabella Mendes Choukaira - 231037692
- Tiago Scherrer Tavares de Lyra - 190048549

---

## Guia de Manutenção e Deploy da Documentação

A documentação deste projeto foi construída utilizando o [MkDocs](https://www.mkdocs.org/) (com o tema Material). Todo o site público é gerado a partir dos arquivos Markdown (`.md`) localizados na pasta `docs/`. 

Se você for membro do grupo e precisar adicionar novas análises, textos ou evidências da avaliação, siga o fluxo abaixo para que as informações apareçam corretamente no GitHub Pages.

### 1. Preparando o ambiente (Primeira vez)
Se for a sua primeira vez editando o repositório na sua máquina, certifique-se de ter o Python instalado e instale o construtor do site via terminal:
```bash
pip install mkdocs-material

```

### 2. Editando e testando localmente

Para visualizar as alterações em tempo real antes de enviar para o repositório oficial:

1. Faça as edições necessárias nos arquivos dentro da pasta `docs/`.
2. Na raiz do projeto (onde está o arquivo `mkdocs.yml`), execute o servidor de testes:
```bash
    mkdocs serve

```


3. Abra o navegador no endereço `http://127.0.0.1:8000`. O site atualizará sozinho a cada alteração salva.

### 3. Publicando as alterações (Deploy para o Pages)

**Atenção:** O GitHub Pages deste projeto está configurado para ler a branch `gh-pages`. **Nunca** envie arquivos manualmente para lá. Todo o processo é automatizado.

Quando terminar de editar e quiser que o conteúdo vá para o ar no site oficial, interrompa o servidor local (pressionando `Ctrl + C` no terminal) e execute:

```bash
mkdocs gh-deploy

```

**O que esse comando faz?**
Ele vai ler todos os textos da pasta `docs/`, transformar tudo em um site HTML estilizado e empurrar o resultado automaticamente para a branch `gh-pages`. Em cerca de 1 a 2 minutos, o GitHub atualizará o link público do projeto com as novas informações!
