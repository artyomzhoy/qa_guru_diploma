import os.path


def env_path():
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if os.path.exists(os.path.join(main_path, '.env')):
        return os.path.join(main_path, '.env')
    else:
        return os.path.join(main_path, '.env.public')
