# HTTPS-Verification

Um script em Python para verificar se um site utiliza HTTPS e se o certificado SSL é válido. Este projeto é ideal para desenvolvedores, administradores de sistemas ou qualquer pessoa interessada em segurança da informação.

## 🚀 Funcionalidades

- Verifica se um site usa HTTPS.
- Valida o certificado SSL do site.
- Salva os resultados em um arquivo JSON para consultas futuras.
- Fácil de usar e configurar.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- **Python 3.x**: [Baixar Python](https://www.python.org/downloads/)
- **Bibliotecas Python**:
  - `requests`
  - `certifi`

Para instalar as bibliotecas, execute:

```bash
pip install requests certifi

🛠️ Como Usar

    Clone o repositório:
    bash
    Copy

    git clone https://github.com/ArthurTorres11/HTTPS-Verification.git

    Navegue até a pasta do projeto:
    bash
    Copy

    cd HTTPS-Verification

    Execute o script:
    bash
    Copy

    python https_web.py

    Digite a URL do site que deseja verificar. Por exemplo:
    Copy

    Digite a URL do site (ex: www.google.com): https://www.google.com

    O script exibirá o resultado no terminal e salvará os detalhes em um arquivo JSON (resultados_ssl.json).

📂 Estrutura do Projeto
Copy

HTTPS-Verification/
├── https_web.py          # Script principal
├── resultados_ssl.json   # Arquivo de saída com os resultados
├── README.md             # Este arquivo
└── requirements.txt      # Lista de dependências (opcional)

📝 Exemplo de Saída

Após executar o script, você verá algo como:
Copy

Digite a URL do site (ex: www.google.com): https://www.google.com

https://www.google.com: ✅ O site é seguro (HTTPS) e o certificado SSL é válido.
Resultado salvo em resultados_ssl.json

O arquivo resultados_ssl.json conterá:
json
Copy

[
    {
        "url": "https://www.google.com",
        "seguro": true,
        "mensagem": "✅ O site é seguro (HTTPS) e o certificado SSL é válido.",
        "data_verificacao": "2023-10-25 14:30:45"
    }
]

🤝 Como Contribuir

Contribuições são bem-vindas! Siga estas etapas:

    Faça um fork do projeto.

    Crie uma nova branch com sua feature ou correção:
    bash
    Copy

    git checkout -b minha-feature

    Faça commit das suas alterações:
    bash
    Copy

    git commit -m "Adicionando nova funcionalidade"

    Envie para o repositório remoto:
    bash
    Copy

    git push origin minha-feature

    Abra um Pull Request no GitHub.

📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
👨‍💻 Autor

    Arthur Torres

        GitHub: ArthurTorres11

        LinkedIn: www.linkedin.com/in/arthur-torres-3223a1325

🌟 Agradecimentos

    À comunidade Python por fornecer ferramentas incríveis.

    Aos mantenedores das bibliotecas requests e certifi.
