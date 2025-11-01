from setuptools import setup, find_packages

setup(
    name="pygram-bot",
    version="0.1.0",
    description="Oddiy Telegram bot framework",
    author="Saparov Mehroj",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.8",
)
