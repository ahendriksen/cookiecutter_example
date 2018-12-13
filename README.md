# cookiecutter example

Python CI CWI boilerplate package.


* Free software: GNU General Public License v3
* Documentation: [https://ahendriksen.github.io/cookiecutter_example]


## Readiness

The author of this package is in the process of setting up this
package for optimal usability. The following has already been completed:

- [X] Documentation
    - Documentation has been generated using `make docs`, committed,
        and pushed to GitHub.
	- GitHub pages have been setup in the project settings
	  with the "source" set to "master branch /docs folder".
- [X] An initial release
	- In `CHANGELOG.md`, a release date has been added to v0.1.0 (change the YYYY-MM-DD).
	- The release has been marked a release on GitHub.
	- For more info, see the [Software Release Guide](https://cicwi.github.io/software-guidelines/software-release-guide).
- [X] A conda package
	- Required packages have been added to `setup.py`, for instance,
	  ```
	  requirements = [ ]
	  ```
	  Has been replaced by
	  ```
	  requirements = [
	      'sacred>=0.7.2'
      ]
      ```
	- All "conda channels" that are required for building and
      installing the package have been added to the
      `Makefile`. Specifically, replace
	  ```
      conda_package: install_dev
      	conda build conda/
      ```
	  by
	  ```
      conda_package: install_dev
      	conda build conda/ -c some-channel -c some-other-channel
      ```
    - Conda packages have been built successfully with `make conda_package`.
	- These conda packages have been uploaded to [Anaconda](https://anaconda.org).
	- The installation instructions (below) have been updated.

## Index of common actions
### Documentation
- Add initial documentation
- Update documentation
- Add documentation to your module
### README
- Update installation instructions
### Modules
- Make submodules easier to reach
### Testing
- Add a test to your program
### Examples
- Make a simple example
### Style
- Automatically improve code layout
### (Conda) Packaging and requirements
- Create a Conda package
- Add Astra dependency
- Add PyTorch dependency
- Add a 'normal' dependency
### Releasing and Changelog
- Create an initial release
- Update unreleased section in CHANGELOG.md
- Create new release

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
