import os

with open('template/README.md', 'r') as f:
    readme_text = f.read()

site = input('Please enter site name:')
project_name = input('Please enter project name: ')
project_id = input('Please enter project id: ')
project_url = input('Please enter project url: ')

project_dir = os.path.join('src', project_id)
if not os.path.exists(project_dir):
    os.mkdir(project_dir)
    readme_text = \
        readme_text.format(site,project_name,project_url)
    with open(os.path.join(project_dir,'README.md'),'w') as f:
        f.write(readme_text)
else:
    raise ValueError('This project exists.')