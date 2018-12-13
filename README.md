# cookiecutter example

Python CI CWI boilerplate package.


* Free software: GNU General Public License v3
* Documentation: [https://ahendriksen.github.io/cookiecutter_example]

## Index of common actions
### Documentation
- Add initial documentation [link](https://github.com/ahendriksen/cookiecutter_example/commit/01e30ce0a44d4f06f6c34d5d3fcb5ef82acde7fc)
- Update documentation [link](https://github.com/ahendriksen/cookiecutter_example/commit/5d930a83956d21937794b7f6e51e3d14e3bc9c01)
- Add documentation to your module (TODO)
### README
- Update installation instructions [link](https://github.com/ahendriksen/cookiecutter_example/commit/1c7cc9063e9a81f76725d07b0c78f4c74b1b9ce0)
### Modules
- Make submodules easier to reach (TODO)
### Testing
- Add a test to your program (TODO)
### Examples
- Make a simple example (TODO)
### Style
- Automatically improve code layout (TODO)
### (Conda) Packaging and requirements
- Create a Conda package [link](https://github.com/ahendriksen/cookiecutter_example/commit/1c7cc9063e9a81f76725d07b0c78f4c74b1b9ce0)
- Add Astra dependency [link](https://github.com/ahendriksen/cookiecutter_example/commit/49cc185ae34b2a05572da4f0b664d7775f14d0f2)
- Add PyTorch dependency (TODO)
- Add a 'normal' dependency (TODO)
### Releasing and Changelog
- Create an initial release [link](https://github.com/ahendriksen/cookiecutter_example/commit/55167577f7c28450d212d4d6a8eacdcb542db9a0)
- Update unreleased section in CHANGELOG.md [link](https://github.com/ahendriksen/cookiecutter_example/commit/1444cf0a3c7536648c3c3e4ec1aced34ab0b46a8)
- Create new release [link](https://github.com/ahendriksen/cookiecutter_example/commit/547c14a563d615f9c3511783190c3f57929ec4a7)


## Overview of source tree

The following files are present in a fresh cookiecutter package:
```
├── CHANGELOG.md				# contains the changelog
├── conda						# contains conda packaging metadata
│   ├── build.sh
│   ├── conda_build_config.yaml
│   ├── meta.yaml
├── CONTRIBUTING.rst			# Can be used to guide contributions
├── cookiecutter_example		# Main source code directory
│   ├── cookiecutter_example.py # main module
│   ├── __init__.py				# module dir
├── docs						# Automatically generated documentation
├── doc_sources					# Source files for documentation
│   ├── changelog.md
│   ├── conf.py
│   ├── cookiecutter_example.rst
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── modules.rst
│   └── readme.md
├── examples					# Example scripts
│   └── getting_started.py
├── LICENSE.md					# license
├── Makefile					# Makefile: contains common `make` commands
├── README.md					# README
├── setup.cfg					# Contains some python tooling-specific configuration
├── setup.py					# Contains the packaging information for the package
└── tests						# Contains tests
    ├── __init__.py
    └── test_cookiecutter_example.py
```

## Getting Started

It takes a few steps to setup cookiecutter example on your
machine. We recommend installing
[Anaconda package manager](https://www.anaconda.com/download/) for
Python 3.

### Installing with conda

Simply install with:
```
conda install -c aahendriksen -c astra-toolbox/label/dev cookiecutter_example
```
or, if you prefer a stable version of astra-toolbox:
```
conda install -c aahendriksen -c astra-toolbox cookiecutter_example
```

### Installing from source

To install cookiecutter example, simply clone this GitHub
project. Go to the cloned directory and run PIP installer:
```
git clone https://github.com/ahendriksen/cookiecutter_example.git
cd cookiecutter_example
conda install -c astra-toolbox astra-toolbox
# If you want the development version of astra, use:
# conda install -c astra-toolbox/label/dev astra-toolbox
pip install -e .
```

### Running the examples

To learn more about the functionality of the package check out our
examples folder.

## Authors and contributors

* **Allard Hendriksne ** - *Initial work*

See also the list of [contributors](https://github.com/ahendriksen/cookiecutter_example/contributors) who participated in this project.

## How to contribute

Contributions are always welcome. Please submit pull requests against the `master` branch.

If you have any issues, questions, or remarks, then please open an issue on GitHub.

## License

This project is licensed under the GNU General Public License v3 - see the [LICENSE.md](LICENSE.md) file for details.
