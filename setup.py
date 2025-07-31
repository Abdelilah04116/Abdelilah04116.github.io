from setuptools import setup, find_packages

setup(
    name="portfolio",
    version="1.0.0",
    description="Portfolio personnel avec chatbot IA",
    author="Abdelilah Ourti",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.3.0",
        "Flask-CORS>=4.0.0",
        "python-dotenv>=1.0.0",
        "langchain>=0.0.350",
        "langchain-community>=0.0.10",
        "langchain-google-genai>=0.0.6",
        "google-generativeai>=0.3.2",
        "faiss-cpu>=1.7.4",
        "numpy>=1.21.0",
        "pypdf>=3.15.0",
        "tiktoken>=0.5.0",
        "gunicorn>=20.1.0",
    ],
    python_requires=">=3.11",
) 