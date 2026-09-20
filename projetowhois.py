import whois as w
def scan_dominio():
    domain = input("Digite o domínio a ser escaneado:")
    print(f"Escaneando o domínio:{domain}")
    data = w.whois(domain)
    print(data)
    return data
scanner = scan_dominio()
