# Administrator documentation

## Dependencies

The cloud-provider depends on PyYAML and Mako, which are already included as
dependencies for binary packages and when installing from source.

For running the cloud-provider in a production environment, depending on your
setup you will might need for OpenStack to install python-novaclient.

## Binary packages

Packages are available at the [INDIGO repository](http://repo.indigo-datacloud.eu).
Use the appropriate repository for your distribution and install using the usual tools.

* ubuntu package: python-cloud-info-provider-indigo
* RHEL 7 package: cloud-info-provider-indigo
