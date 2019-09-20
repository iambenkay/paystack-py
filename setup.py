from setuptools import setup

with open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paystack-py',
    version='1.0.3',
    packages=['paystack_py'],
    long_description=long_description,
    url='https://github.com/iambenkay/paystack-py',
    license='Apache 2.0',
    author='benkay',
    author_email='benjamincath@gmail.com',
    description='For completing, initializing and verifying paystack transactions',
    install_requires=[
        'requests',
    ],
    zip_safe=False,
)
