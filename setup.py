import setuptools

with open("README.md", "r" , encoding="utf-8") as f:
    long_des = f.read()

__version__= "0.0.1"

REPO_NAME = "Kidney_Disease_Classification"
AUTHOR_USER_NAME = "kru2710shna"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "krushna27doc@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "package for python cnnclassifier",
    long_description=long_des,
    long_description_content_type= "text/makrdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src")
    
    
    
    
    
    
    
    
)