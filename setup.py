from setuptools import setup, find_packages
setup(
    name='regressao_linear_brasil',
    version='0.0.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        # ... outras dependências
    ],
    description='Uma classe para Regressão Linear em português, contendo as principais métricas da abordagem como métodos.',
    author='Bruno Rodrigues Carloto',
    author_email='brunnocarlotosjob@gmail.com',
    url='https://github.com/bruno-rodrigues-carloto/regressao-linear-brasil',
    python_requires='>=3.6',
)
