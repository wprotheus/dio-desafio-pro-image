from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dio-pro-image",
    version="1.0.1",
    author="wprotheus",
    author_email="wellneto@hotmail.com",
    description="Praticando processamento de imagem.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wprotheus/dio-desafio-pro-image.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)