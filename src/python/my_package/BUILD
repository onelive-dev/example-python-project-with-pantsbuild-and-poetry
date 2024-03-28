python_sources(
  name="my_package",
  sources=["*.py"],
  dependencies=[
      "external/python:poetry#requests",
  ],
)

pex_binary(
  name="my_main",
  entry_point="my_package.my_module:main",
)
