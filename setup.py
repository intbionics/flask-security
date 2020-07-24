"""Simple security for Flask apps."""

import re
from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("flask_security/__init__.py") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# tests_require = [
    # "Flask-Mail>=0.9.1",
    # "Flask-Mongoengine>=0.9.5",
    # "peewee>=3.11.2",
    # "Flask-SQLAlchemy>=2.4.4",
    # "argon2_cffi>=19.1.0",
    # "bcrypt>=3.1.5",
    # "check-manifest>=0.25",
    # "coverage>=4.5.4",
    # "cryptography>=2.3.1",
    # "mongoengine>=0.18.0",
    # "mongomock>=3.19.0",
    # "msgcheck>=2.9",
    # "pony>=0.7.11;python_version<'3.9'",
    # "phonenumberslite>=8.11.1",
    # "pre-commit>=2.4.0",
    # "psycopg2>=2.8.4",
    # "pydocstyle>=5.0.0",
    # "pymysql>=0.9.3",
    # "pyqrcode>=1.2",
    # "pytest-cache>=1.0",
    # "pytest-cov>=2.5.1",
    # "pytest>=5.4.0",
    # "sqlalchemy>=1.3.6",
    # "sqlalchemy-utils>=0.34.1",
    # "werkzeug>=0.15.5",
    # "zxcvbn~=4.4.28",
# ]

# extras_require = {
    # "docs": ["Pallets-Sphinx-Themes>=1.2.3", "Sphinx>=3.0.3", "sphinx-issues>=1.2.0"],
    # "tests": tests_require,
# }

# extras_require["all"] = []
# for reqs in extras_require.values():
    # extras_require["all"].extend(reqs)

# setup_requires = ["Babel>=2.8.0", "pytest-runner>=5.2", "twine", "wheel"]

# install_requires = [
    # "Flask>=1.1.1",
    # "Flask-Login>=0.4.1",
    # "Flask-Principal>=0.4.0",
    # "Flask-WTF>=0.14.2",
    # "Flask-BabelEx>=0.9.3",
    # "email-validator>=1.0.5",
    # "itsdangerous>=1.1.0",
    # "passlib>=1.7.2",
# ]

packages = find_packages()

setup(
    name="Flask-Security-Too",
    version=version,
    # description=__doc__,
    long_description=readme,
    keywords="flask security",
    license="MIT",
    author="Matt Wright & Chris Wagner",
    author_email="jwag.wagner+github@gmail.com",
    url="https://github.com/Flask-Middleware/flask-security",
    project_urls={
        "Documentation": "https://flask-security-too.readthedocs.io",
        "Releases": "https://pypi.org/project/Flask-Security-Too/",
        "Code": "https://github.com/Flask-Middleware/flask-security",
        "Issue tracker": "https://github.com/Flask-Middleware/flask-security/issues",
    },
    package_dir={'flask_security': 'src'}
    # packages=packages,
    # zip_safe=False,
    # include_package_data=True,
    # platforms="any",
    # python_requires=">=3.6",
    # extras_require=extras_require,
    # install_requires=install_requires,
    # setup_requires=setup_requires,
    # tests_require=tests_require,
    # classifiers=[
        # "Environment :: Web Environment",
        # "Framework :: Flask",
        # "Intended Audience :: Developers",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
        # "Programming Language :: Python",
        # "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        # "Topic :: Software Development :: Libraries :: Python Modules",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: Implementation :: CPython",
        # "Programming Language :: Python :: Implementation :: PyPy",
        # "Development Status :: 4 - Beta",
    # ],
)
