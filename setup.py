from setuptools import setup, find_packages

setup(
    name="aws-security-monitor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["boto3>=1.26.0", "python-dateutil>=2.8.2"],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-mock>=3.10.0",
            "moto>=4.0.0",
        ],
    },
)
