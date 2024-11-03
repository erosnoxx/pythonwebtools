Claro! Aqui está a versão revisada do seu documento, agora com um sumário para facilitar a navegação. Isso ajudará os leitores a encontrar rapidamente a seção desejada.

### Sumário

1. [Exemplos de Uso](#exemplos-de-uso)
   - [Validação de Campos de Entrada](#validação-de-campos-de-entrada)
   - [Validação de Número de Telefone](#validação-de-número-de-telefone)
   - [Validação de CPF](#validação-de-cpf)
   - [Validação de CNPJ](#validação-de-cnpj)
   - [Validação de E-mail](#validação-de-e-mail)
   - [Validação de Senha](#validação-de-senha)
   - [Utilitários Criptográficos](#utilitários-criptográficos)
   - [Utilitários de Hash](#utilitários-de-hash)

---

### Exemplos de Uso

#### Validação de Campos de Entrada
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Inicializa o validador
validate = ValidatorUtils()

# Dados de entrada a serem validados
input_data = {
    'nome': 'João',
    'idade': 30,
    'email': 'joao@exemplo.com'
}

# Campos obrigatórios e seus tipos esperados
required_fields = {
    'nome': str,
    'idade': int,
    'email': str
}

# Valida os dados de entrada
erros = validate.validate_input(input_data, required_fields)

# Exibe mensagens de erro, se houver
if erros:
    for erro in erros:
        print(f"Erro: {erro}")
else:
    print("Todos os campos são válidos!")
```

#### Validação de Número de Telefone
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Formato de número de telefone: DDD seguido por 9 e 8 dígitos (sem espaços)
validate = ValidatorUtils()
telefone_valido = '11981749632'

# Verifica se o número de telefone é válido
is_valid = validate.phone_number_validator(telefone_valido)  # Retorna True se válido, False se inválido
print(f"Telefone válido: {is_valid}")
```

#### Validação de CPF
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Formato de CPF: 11 dígitos (apenas números)
validate = ValidatorUtils()
cpf_valido = '12345678909'

# Verifica se o CPF é válido
is_valid = validate.cpf_validator(cpf_valido)  # Retorna True se válido, False se inválido
print(f"CPF válido: {is_valid}")
```

#### Validação de CNPJ
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Formato de CNPJ: 14 dígitos (apenas números)
validate = ValidatorUtils()
cnpj_valido = '12345678000195'

# Verifica se o CNPJ é válido
is_valid = validate.cnpj_validator(cnpj_valido)  # Retorna True se válido, False se inválido
print(f"CNPJ válido: {is_valid}")
```

#### Validação de E-mail
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Formato de e-mail: padrão de e-mail (ex: usuario@exemplo.com)
validate = ValidatorUtils()
email_valido = 'usuario@exemplo.com'

# Verifica se o e-mail é válido
is_valid = validate.email_validator(email_valido)  # Retorna True se válido, False se inválido
print(f"E-mail válido: {is_valid}")
```

#### Validação de Senha
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Regras da senha: mínimo de 8 caracteres, incluindo letras e números
validate = ValidatorUtils()
senha_valida = 'Senha123'

# Verifica se a senha é válida
is_valid = validate.password_validator(senha_valida)  # Retorna True se válida, False se inválida
print(f"Senha válida: {is_valid}")
```

#### Utilitários Criptográficos
```python
from pythonwebtools.services.CryptService import CryptService

# Inicializa o serviço de criptografia
crypt_service = CryptService()

# Texto a ser criptografado
texto_original = "Texto secreto"

# Criptografa o texto
texto_criptografado = crypt_service.encrypt(texto_original)
print(f"Texto criptografado: {texto_criptografado}")

# Descriptografa o texto
texto_descriptografado = crypt_service.decrypt(texto_criptografado)
print(f"Texto descriptografado: {texto_descriptografado}")
```

#### Utilitários de Hash
```python
from pythonwebtools.services.HashService import HashService

hash_service = HashService()

# Gerando hash
senha = 'SenhaForte5@'
senha_hasheada = hash_service.hash_password(senha)

# Verificando o hash
is_valid = hash_service.verify_password(
    hashed_password=senha_hasheada,
    provided_password=senha) # True se for válida, False se for inválida
```

---
