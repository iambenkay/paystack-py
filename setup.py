from setuptools import setup

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paystack-py',
    version='1.0.2',
    packages=['paystack_py'],
    url='https://github.com/iambenkay/paystack-py',
    license='Apache 2.0',
    author='benkay',
    author_email='benjamincath@gmail.com',
    description='For completing, initializing and verifying paystack transactions',
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    long_description_content_type='text/markdown',
    long_description=long_description,
)
