from setuptools import setup

setup(
    name='paystack-py',
    version='1.0.5',
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
)
