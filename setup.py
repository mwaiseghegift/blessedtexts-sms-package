from setuptools import setup, find_packages

setup(
    name="blessedtexts_sms",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python client for the BlessedTexts SMS API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/blessedtexts_sms",
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
