# Continuous Integration using Azure Pipelines

The main pipeline is `pipeline.yml`, which is a shallow wrapper around some configuration templates.
Those templates in turn drive the right settings into `common.yml`, where the bulk of work is performed.

`common.yml` has a set of parameters it expects:

- name: Required; name of the configuration (will be used as an ID, so make it alphanumeric and with no spaces)
- platform: Required; one of "Linux" or "Windows" ("macOS" coming)
- settings: Required; name of the settings module to use. Recommend putting these in /.azure-pipelines/ci_settings
- py_3_5: Optional; run tests against Python 3.5?
- py_3_6, py_3_7, py_3_8: Optional; similar to py_3_5
- container_name: Optional: if this build requires a container (usually to talk to a database), put its name here
- container_startup: Optional: if this build requires a container, put its `docker run` string here
- additional_apt_gets: Optional: if the build requires additional `apt-get install`s on Linux, list them here
- additional_requirements: Optional: if the build requires additional requirements.txt installs, point to that requirements.txt file here

`mysql.yml` is a good starting point for adding new container-based configurations.
`sqlite.yml` is a good starting point for adding new multi-platform configurations (it builds on Windows and Linux).
