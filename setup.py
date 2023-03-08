import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alexa_config",
    version="0.1.0",
    author="flens74",
    author_email="your@email.com",
    description="Integration for configuring Alexa devices in Home Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flens74/alexa_config",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.0.0",
        "pytz>=2021.1"
    ]
)
