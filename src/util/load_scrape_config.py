import json

def _config_reader(file_path):
    
    config_json = {}
    with open(config_path, 'r') as config_file:
        config_json = json.load(config_file)
    
    return config_json

def get_scrape_config()
    config_path = os.path.join(os.curdir,'src', 'config', 'scrape.config')
    return _config_reader(config_path)

def get_rss_config()
    config_path = os.path.join(os.curdir,'src', 'config', 'rss.config')
    return _config_reader(config_path)