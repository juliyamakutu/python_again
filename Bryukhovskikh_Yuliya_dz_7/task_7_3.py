import os
import sys
import shutil


TEMPLATES_DIR = 'templates'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <project_name>')
    project_dir = os.path.abspath(sys.argv[1])
    templates_dir = os.path.join(project_dir, TEMPLATES_DIR)
    if not os.path.exists(project_dir):
        raise FileNotFoundError('Нет такого проекта')
    if os.path.exists(templates_dir):
        shutil.rmtree(templates_dir)
    os.mkdir(templates_dir)
    for path, dirs, files in os.walk(project_dir):
        for dir in dirs:
            if dir == TEMPLATES_DIR:
                shutil.copytree(os.path.join(path, dir), templates_dir, dirs_exist_ok=True)