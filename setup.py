import setuptools
with open("README.md","r",encoding="utf -8") as f:
    long_description = f.read()


__version__="0.0.2"

REPO_NAME="IPYNBrenderer"
AUTHOR_USER_NAME ="akhilpratap620"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL ="sakhilpratap620@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small package",
    long_decription=long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues"
        },

        package_dir = {"":"src"},
        packages =setuptools.find_packages(where="src")
    

)
