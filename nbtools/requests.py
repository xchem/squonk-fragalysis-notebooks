
STACKS = { "staging":"https://fragalysis.xchem.diamond.ac.uk", "production": "https://fragalysis.diamond.ac.uk" }

def _request(stack: str = "production"):
    import requests
    from urllib.parse import urljoin
    
    url_root = STACKS[stack]
    
    
    

def target_list():
    
    import requests
    
    raise NotImplementedError

def download():
    raise NotImplementedError