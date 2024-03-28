# Pants with Poetry example

Project structure

```
├── README.md
├── external <folder name is defined by you>
│   └── python <folder name ref to python projects>
│       ├── BUILD
│       ├── poetry.lock <generate after install some dep e.g: poetry add requests>
│       └── pyproject.toml <generate by poetry init>
├── pants.toml
├── src
│   └── python
│       └── my_package
│           ├── BUILD
│           ├── __init__.py
│           └── my_module.py
└── tests
    └── python
        └── my_package
            ├── BUILD
            ├── __init__.py
            └── test_my_module.py

```    

## Steps for reproduce & work with this project structure

We need have Poetry installed 

- https://python-poetry.org/docs/#installation

`brew install poetry`

Let create a folder with the sub folder `/python` to have all deps

- `mkdir -r external/python`
- `cd external/python & poetry init`

Installs a project dependency

- `poetry add requests`

We need to init pants at the root dir

`pants`

this commant will create a pants.toml file similiar to this:

```
[GLOBAL]
pants_version = "2.19.1"
```

update it as this:

```
[GLOBAL]
pants_version = "2.19.1"
backend_packages = ["pants.backend.python"]

[python]
interpreter_constraints = ["==3.8.*", "==3.9.*"]
```


## run a function e.g: main 

`pants run src/python/my_package:my_main`

## Test Command

`pants test tests/python/my_package:test_my_module`

