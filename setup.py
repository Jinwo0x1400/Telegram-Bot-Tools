from setuptools import setup, find_packages

setup(
    name='telegramtools',
    version='1.0.0',
    description='Telegram Bot Tools: Scraper, Adder, Sender using Telethon',
    author='Jinwoo',
    packages=find_packages(),
    py_modules=['auth', 'scrape', 'adder', 'sender'],
    install_requires=[
        'telethon>=1.28.5'
    ],
    entry_points={
        'console_scripts': [
            'telegram-auth = auth:main',
            'telegram-scrape = scrape:main',
            'telegram-add = adder:main',
            'telegram-send = sender:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
