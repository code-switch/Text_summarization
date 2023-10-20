import setuptools

with open('README.md', 'r', encoding ='utf-8') as f:  # used to read the README.md file & create the package intro page on PyPI webpage
    long_description =  f.read()

__version__ = "0.0.0" # version of your custom package 

REPO_NAME = 'Text-Summarizer-Project' # github repo name
AUTHOR_USER_NAME = 'code-switch' # github username
SRC_REPO = 'textSummarizer'  # local repo name given just inside 'src' 
AUTHOR_EMAIL = 'abhi.learner07@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= 'small python package for NLP app',
    long_description=long_description,
    long_description_content='text/markdown',
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages = setuptools.find_packages(where='src')

)

