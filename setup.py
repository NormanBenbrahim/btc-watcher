from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1.0",
    install_requires=[
        "fastapi==0.60.1",
        "httpx==0.13.3",
        "pydantic==1.6.1",
        "uvicorn==0.11.7",
        "pytz==2020.4",
        "requests==2.23.0"
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
)