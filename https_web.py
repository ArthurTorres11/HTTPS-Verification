import certifi
import requests
import json
from datetime import datetime

def is_secure_website(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url  

        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()  

        if response.url.startswith('https://'):
            return True, "O site é seguro (HTTPS) e o certificado SSL é válido."
        else:
            return False, "O site redirecionou para uma conexão não segura (HTTP)."
    
    except requests.exceptions.SSLError:
        return False, "Erro no certificado SSL: o site não é seguro."
    except requests.exceptions.RequestException as e:
        return False, f"Erro ao acessar o site: {str(e)}"

def salvar_resultado_json(url, resultado, mensagem, arquivo="resultados_ssl.json"):
    dados = {
        "url": url,
        "seguro": resultado,
        "mensagem": mensagem,
        "data_verificacao": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    try:
        with open(arquivo, "r") as f:
            dados_existentes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_existentes = []
    
    dados_existentes.append(dados)
    
    with open(arquivo, "w") as f:
        json.dump(dados_existentes, f, indent=4)
    
    print(f"Resultado salvo em {arquivo}")

if __name__ == "__main__":
    website_url = input("Digite a URL do site: ").strip()
    secure, message = is_secure_website(website_url)
    print(f"\n{website_url}: {message}")

    salvar_resultado_json(website_url, secure, message)