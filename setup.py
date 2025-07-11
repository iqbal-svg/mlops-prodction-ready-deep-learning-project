# setup.py

import setuptools

# Read the content of README.md to show as long description on PyPI
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"
REPO_NAME = "mlops-prodction-ready-deep-learning-project"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "cnnClassifier"  # The actual source folder inside 'src/'
AUTHOR_EMAIL = "entbappy73@gmail.com"

# The main setup() function
setuptools.setup(
    name=SRC_REPO,                        # Name of your package
    version=__version__,                 # Version number
    author=AUTHOR_USER_NAME,            # Author name
    author_email=AUTHOR_EMAIL,          # Author email
    description="A small python package for CNN app",  # Short description
    long_description=long_description,   # Full description from README.md
    long_description_content="text/markdown",  # Tells PyPI that README is in Markdown

    # GitHub project homepage
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    # Additional URLs like bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    # Tells setuptools to look for packages inside 'src/' directory
    package_dir={"": "src"},

    # Automatically find all packages in the 'src/' folder
    packages=setuptools.find_packages(where="src"),
)