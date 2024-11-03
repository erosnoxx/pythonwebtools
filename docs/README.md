# PythonWebTools

**PythonWebTools** is a utility library for Python focused on enhancing your web applications with common utilities and helpers.

## Features

- Email validation
- CPF and CNPJ validation
- Password validation
- Phone number validation
- Cryptographic utilities

## Installation

You can install PythonWebTools using pip. It is recommended to use a virtual environment.

```bash
pip install pythonwebtools
```

## Usage

To use **PythonWebTools** in your application, you need to import the required utilities from the library. Below are examples of how to use each feature.

## Email Validation

```python
from pythonwebtools.utils.ValidatorUtils import ValidatorsUtil

validator = ValidatorsUtil()

try:
    is_valid = validator.validate_email("example@email.com")
    print("Email is valid:", is_valid)
except Exception as e:
    print("Invalid email:", str(e))
```

## CPF Validation

```python
from pythonwebtools.utils.ValidatorUtils import ValidatorsUtil

validator = ValidatorsUtil()

cpf = "123.456.789-09"  # Example CPF
is_valid_cpf = validator.validate_cpf(cpf)
print("CPF is valid:", is_valid_cpf)
```

## CNPJ Validation

```python
from pythonwebtools.utils.ValidatorUtils import ValidatorsUtil

validator = ValidatorsUtil()

cnpj = "12.345.678/0001-95"  # Example CNPJ
is_valid_cnpj = validator.validate_cnpj(cnpj)
print("CNPJ is valid:", is_valid_cnpj)
```

## Password Validation

```python
from pythonwebtools.utils.ValidatorUtils import ValidatorsUtil

validator = ValidatorsUtil()

password = "StrongPassword123!"  # Example password
is_valid_password = validator.validate_password(password)
print("Password is valid:", is_valid_password)
```

## Phone Number Validation

```python
from pythonwebtools.utils.ValidatorUtils import ValidatorsUtil

validator = ValidatorsUtil()

phone_number = "5511997027812"  # Example phone number. Only works with Brazilian phone numbers for now
is_valid_phone = validator.phone_number_validator(phone_number)
print("Phone number is valid:", is_valid_phone)
```

## Cryptographic Utilities

For cryptographic functionalities, you can use the cryptography utilities provided in the **PythonWebTools** library. Below is an example of how to hash a password:

```python
from pythonwebtools.services.HashService import HashService

hash_service = HashService()

password = "my_secure_password"
hashed_password = hash_service.hash_password(password)
print("Hashed password:", hashed_password)

# To verify the password
is_password_correct = hash_service.verify_password(hashed_password, password)
print("Is password correct:", is_password_correct)
```