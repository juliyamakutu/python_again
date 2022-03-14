import os
import sys


PROJECT_STRUCT = {
    'settings': {
        '__init__.py': None,
        'dev.py': None,
        'prod.py': None,
    },
    'mainapp': {
        '__init__.py': None,
        'models.py': None,
        'views.py': None,
        'templates': {
            'mainapp': {
                'base.html': None,
                'index.html': None,
            }
        }
    },
    'authapp': {
        '__init__.py': None,
        'models.py': None,
        'views.py': None,
        'templates': {
            'authapp': {
                'base.html': None,
                'index.html': None,
            }
        }
    },
}


def create_struct(path: str, data: dict) -> None:
    for key, val in data.items():
        current = os.path.join(path, key)
        if isinstance(val, dict):
            if not os.path.exists(current):
                os.mkdir(current)
            create_struct(os.path.join(path, key), val)
        else:
            if not os.path.exists(current):
                open(current, 'w').close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <project_name>')
    project_dir = os.path.abspath(sys.argv[1])
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
    create_struct(project_dir, PROJECT_STRUCT)