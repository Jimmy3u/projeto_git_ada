# Desafio Git Ada

Para o desafio foi utlizado um script em python que le o arquivo posts.json que se encontra na pasta docs, para gerar paginas estaticas em html.
Estrutura arquivo de Posts Json:
~~~json
    {
        "titulo" : "<Titulo Do Post>",
        "slug": "<slug do post>",
        "autor" : "<Nome>",
        "data" : "<data>",
        "content" : "<O Arquivo do Post em markdown>" 
    }
~~~
Os arquivos em markdown utilizados para gerar os conteudos ficam localizados na pasta `docs/posts`, porem o script pode ser alterado facilmente para utilizar o esquema que mais lhe agradar. 
Tambem é utilizado o Jinja para criação de templates simples e com possibilidade de alteração no futuro.