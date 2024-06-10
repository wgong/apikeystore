# apikeystore

This package is a python utility to store and retrieve API Keys.

## Install 

### Install from PyPi
```
pip install api-key-store
```


### Install from source
```
pip install -e .
```

## How to use
- Update `stores.yaml` with your API keys and save to a secure location (e.g. ~/.api_keys/stores.yaml)

- Use in python
```
from api_key_store import ApiKeyStore
aks = ApiKeyStore("./stores.yaml")

print(f"API Providers: {aks.list_api_providers()}")

p = "OPENAI"
key = aks.get_api_key(provider=p)
print(f"{p} : {key}")

p = "GOOGLE/PALM"
key = aks.get_api_key(provider=p)
print(f"{p} : {key}")

```