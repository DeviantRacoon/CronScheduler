import os


def load_dotenv(path='.env'):
    """
    Load the variables from the dotenv file and return them as a dictionary.
    """
    dotenv = {}
    if os.path.exists(path):
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                key, value = line.split('=')
                key = key.strip()
                value = value.strip()
                dotenv[key] = value
    return dotenv


if __name__ == '__main__':
    dotenv = load_dotenv()
    print(dotenv['PHONES_NUMBERS'].split(','))
    print(dotenv['SERVICE_SMS'])

