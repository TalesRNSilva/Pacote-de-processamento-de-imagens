from setuptools import setup, find_packages
with open("README.md", 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "banco-POO",
    version = '0.0.1',
    author = 'Tales',
    author_email = 'talesrnsilva@gmail.com',
    description = 'Teste de formação de pacotes',
    loong_description = page_description,
    long_description_content_type= "text/markdown",
    url = 'https://github.com/TalesRNSilva/Pacote-de-processamento-de-imagens/',
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.10'
)