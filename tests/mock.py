import random
import string
import requests
from faker import Faker

fake = Faker()

def generate_strong_password(length=12) -> str:
    if length < 8:
        raise ValueError("The password length must be at least 8 characters.")

    password_characters = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) + 
        random.choice(string.punctuation) 
    )

    remaining_characters = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=length - len(password_characters)
    ))

    password = password_characters + remaining_characters
    return ''.join(random.sample(password, len(password)))

def generate_random_text(length=20) -> str:
    if length <= 0:
        raise ValueError("The length  must be greater than 0.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_faker_sentence() -> str:
    return fake.sentence()

def generate_random_phone_number() -> str:
    area_code = random.randint(10, 99)
    number = f"9{random.randint(10000000, 99999999)}"
    return f"{area_code}{number[:5]}{number[5:]}"

def generate_random_cpf() -> str:
    return f"{random.randint(100000000, 999999999)}{random.randint(0, 9)}{random.randint(0, 9)}"

def generate_random_cnpj() -> str:
    return f"{random.randint(10000000, 99999999)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

def generate_valid_cpf() -> str:
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.4devs.com.br',
        'Referer': 'https://www.4devs.com.br/gerador_de_cpf',
        'Connection': 'keep-alive',
    }
    data = {
        'acao': 'gerar_cpf',
        'pontuacao': 'S',
        'cpf_estado': ''
    }

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to generate CPF: {response.status_code} - {response.text}")

def generate_valid_cnpj() -> str:
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.4devs.com.br',
        'Referer': 'https://www.4devs.com.br/gerador_de_cnpj',
        'Connection': 'keep-alive',
    }
    data = {
        'acao': 'gerar_cnpj',
        'pontuacao': 'S'
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to generate CNPJ: {response.status_code} - {response.text}")
