from jinja2 import Environment, FileSystemLoader, select_autoescape



# file_loader = FileSystemLoader()
#
#
#
# t = Template("""
#     <h1>{% block title %}HELLO!{% endblock %}</h1>
#     """)
#
def create_message(top):
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    tm = env.get_template('index.html')
    message = tm.render(items=top)
    with open('/Users/aitegin/Desktop/course/mountain', 'w') as fh:
        fh.write(message)
    return message