# redditflow.py

import os

def main(api_type, config):
    
    if api_type == "text":
        
        print(f"Running Text API with config: {config}")
    elif api_type == "image":
        
        print(f"Running Image API with config: {config}")
    else:
        print(f"Unknown API_TYPE: {api_type}")
    

if __name__ == "__main__":
    api_type = input("Enter API type (text/image): ").strip()
    config = input("Enter configuration (as key=value pairs or JSON): ").strip()
    
    main(api_type, config)
