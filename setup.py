from setuptools import setup, find_packages

setup(
    name="blessedtexts_sms",
    version="0.1.0",
    author="Gift Mwaiseghe",
    author_email="mwaiseghe.dev@gmail.com",
    description="A Python client for the BlessedTexts SMS API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mwaiseghegift/blessedtexts-sms-package",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
