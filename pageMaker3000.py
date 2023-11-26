import markdown
import json

with open('posts.json') as json_file:
    dados = json.load(json_file)
# Abre o arquivo markdown
def parse_file(file):
    md = markdown.Markdown(extensions=['fenced_code'])
    file_stream = open(file, "r")
    file_content = file_stream.read()
    html = md.convert(file_content)
    return html

for post in dados:
    print(post["titulo"])
    print(post["autor"])
    print(parse_file(post["arquivo"]))

    