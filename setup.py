from setuptools import setup, find_packages

setup(
    name='pythonwebtools',
    version='0.1.1',
    description='A utility library for Python that provides common validation and cryptographic functions for web development.',
    author='Eros Gabriel Vieira',
    author_email='apenaclaskrr@gmail.com',
    url='https://github.com/erosnoxx/pywebtools',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'email-validator',   # For email validation
        'python-dotenv',     # For loading environment variables from .env files
        'cryptography',      # For cryptographic operations
        'argon2-cffi'       # For secure password hashing
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security :: Cryptography',
    ],
    python_requires='>=3.6',
)