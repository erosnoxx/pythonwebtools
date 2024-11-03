# Table of Contents

1. [Usage Examples](#usage-examples)
   - [Input Field Validation](#input-field-validation)
   - [Phone Number Validation](#phone-number-validation)
   - [CPF Validation](#cpf-validation)
   - [CNPJ Validation](#cnpj-validation)
   - [Email Validation](#email-validation)
   - [Password Validation](#password-validation)
   - [Cryptographic Utilities](#cryptographic-utilities)
   - [Hash Utilities](#hash-utilities)

# Usage Examples

#### Input Field Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Initialize the validator
validate = ValidatorUtils()

# Input data to be validated
input_data = {
    'name': 'João',
    'age': 30,
    'email': 'joao@exemplo.com'
}

# Required fields and their expected types
required_fields = {
    'name': str,
    'age': int,
    'email': str
}

# Validate the input data
errors = validate.validate_input(input_data, required_fields)

# Display error messages, if any
if errors:
    for error in errors:
        print(f"Error: {error}")
else:
    print("All fields are valid!")
```

#### Phone Number Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Phone number format: area code followed by 9 and 8 digits (no spaces)
validate = ValidatorUtils()
valid_phone = '11981749632'

# Check if the phone number is valid
is_valid = validate.phone_number_validator(valid_phone)  # Returns True if valid, False if invalid
print(f"Valid phone: {is_valid}")
```

#### CPF Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# CPF format: 11 digits (only numbers)
validate = ValidatorUtils()
valid_cpf = '12345678909'

# Check if the CPF is valid
is_valid = validate.cpf_validator(valid_cpf)  # Returns True if valid, False if invalid
print(f"Valid CPF: {is_valid}")
```

#### CNPJ Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# CNPJ format: 14 digits (only numbers)
validate = ValidatorUtils()
valid_cnpj = '12345678000195'

# Check if the CNPJ is valid
is_valid = validate.cnpj_validator(valid_cnpj)  # Returns True if valid, False if invalid
print(f"Valid CNPJ: {is_valid}")
```

#### Email Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Email format: standard email (ex: user@example.com)
validate = ValidatorUtils()
valid_email = 'user@example.com'

# Check if the email is valid
is_valid = validate.email_validator(valid_email)  # Returns True if valid, False if invalid
print(f"Valid email: {is_valid}")
```

#### Password Validation
```python
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils

# Password rules: minimum of 8 characters, including letters and numbers
validate = ValidatorUtils()
valid_password = 'Password123'

# Check if the password is valid
is_valid = validate.password_validator(valid_password)  # Returns True if valid, False if invalid
print(f"Valid password: {is_valid}")
```

#### Cryptographic Utilities
```python
from pythonwebtools.services.CryptService import CryptService

# Initialize the cryptography service
crypt_service = CryptService()

# Text to be encrypted
original_text = "Secret text"

# Encrypt the text
encrypted_text = crypt_service.encrypt(original_text)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the text
decrypted_text = crypt_service.decrypt(encrypted_text)
print(f"Decrypted text: {decrypted_text}")
```

#### Hash Utilities
```python
from pythonwebtools.services.HashService import HashService

hash_service = HashService()

# Generating hash
password = 'StrongPassword5@'
hashed_password = hash_service.hash_password(password)

# Verifying the hash
is_valid = hash_service.verify_password(
    hashed_password=hashed_password,
    provided_password=password) # True if valid, False if invalid
```