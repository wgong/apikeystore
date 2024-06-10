"""
TODO:
- encrypt stores.yaml file 

"""

import yaml
from os.path import expanduser
from pathlib import Path

class ApiKeyStore():
    def __init__(self, store_path="~/.api_keys/stores.yaml"):
        file_path = expanduser(store_path) if "~" in store_path else store_path
        with open(Path(file_path), encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)
            self.api_providers = list(self.cfg.keys())
            
    def list_api_providers(self):
        return self.api_providers
        
    def get_provider(self,provider):
        parts = provider.split("/")
        if parts and parts[0] not in self.api_providers:
            raise Exception(f"{parts[0]} not in {self.api_providers}")
            
        for i in range(len(parts)):
            if i==0: 
                p = self.cfg
            if not p: break
            p = p.get(parts[i], {})
        return p
        
    def get_api_key(self, provider="OPENAI", key_name=""):
        p = self.get_provider(provider)
        return p.get("API_KEY", key_name)

if __name__ == "__main__":
    if Path("./stores.yaml").exists():
        aks = ApiKeyStore(store_path="./stores.yaml")
    else:
        aks = ApiKeyStore()
    print(f"API Providers: {aks.list_api_providers()}")
    
    p = "GOOGLE/PALM"
    api_key = aks.get_api_key(p)
    print(f"{p} API Key : {api_key}")
    p = "GOOGLE/VERTEX_AI"
    api_key = aks.get_api_key(p)
    print(f"{p} API Key : {api_key}")
    
    for p in aks.api_providers:
        if p == "GOOGLE":
            continue
        elif p == "HUGGING_FACE":
            for k in ["HF_READ", "HF_WRITE"]:
                api_key = aks.get_api_key(f"{p}/{k}")
                print(f"{p}/{k} API Key : {api_key}")
        else:
            api_key = aks.get_api_key(p)
            print(f"{p} API Key : {api_key}")
                
      
