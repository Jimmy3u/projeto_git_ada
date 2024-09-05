import os
import markdown
import json
from jinja2 import Template

# Gera o HTML do arquivo markdown
def parse_markdown_file(file):
    md = markdown.Markdown(extensions=['fenced_code'])
    file_stream = open(file, "r")
    file_content = file_stream.read()
    file_stream.close()
    html = md.convert(file_content)
    return html

#Salva o arquivo html
def save_html(path ,filename, content):
    output_file = open(f'{path}/{filename}.html', "w")
    output_file.write(content)
    output_file.close()

# Cria a pasta caso não exista
def checkForFolder():
    if not os.path.exists(r'src'):
        os.makedirs(r'src')
        os.makedirs(r'src/media')
        os.makedirs(r'src/posts')


#Le os posts do arquivo json a serem convertidos
with open('docs/posts.json') as json_file:
    dados = json.load(json_file)

#Le o template do post
with open('docs/templates/post.html') as post_template:
    post_template = Template(post_template.read())


checkForFolder()
# Cria os posts individuais
for post in dados:
    html = post_template.render(
        title=post["titulo"],
        autor=post["autor"],
        data=post["data"],
        markdown=parse_markdown_file(f'docs/posts/{post["content"]}')
    )
    save_html("src/posts",post["slug"], html)

# Le o template da pagina com posts e cria ela
with open('docs/templates/blog.html') as blog_template:
    blog_template = Template(blog_template.read())
    save_html("src/", "index", blog_template.render(posts=dados))

