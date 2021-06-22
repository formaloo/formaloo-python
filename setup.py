import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return [
        r for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), 'requirements', *f)).readlines()
        ) if r]


setuptools.setup(
    name="formaloo-cdp",
    version="0.2.3",
    author="Formaloo",
    author_email="info@formaloo.com",
    description="Official SDK to use Formaloo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/formaloo/formaloo-python",
    project_urls={
        "Bug Tracker": "https://github.com/formaloo/formaloo-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=['t', 't.*']),
    python_requires=">=3.6",
    install_requires=reqs('default.txt'),
)
