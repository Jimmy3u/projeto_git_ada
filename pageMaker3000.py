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

#Le os posts do arquivo json a serem convertidos
with open('docs/posts.json') as json_file:
    dados = json.load(json_file)
#Le o template do post
with open('docs/templates/post.html') as post_template:
    post_template = Template(post_template.read())
# Cria os posts individuais
for post in dados:
    html = post_template.render(
        title=post["titulo"],
        autor=post["titulo"],
        data=post["titulo"],
        markdown=parse_markdown_file(f'docs/posts/{post["content"]}')
    )
    print(html)

# Cria a pagina com os posts
with open('docs/templates/blog.html') as blog_template:
    blog_template = Template(blog_template.read())

print(blog_template.render(posts=dados))