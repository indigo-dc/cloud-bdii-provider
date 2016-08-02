# Cloud Information provider

[![BuildStatus](https://travis-ci.org/indigo-dc/cloud-info-provider.svg?branch=master)](https://travis-ci.org/indigo-dc/cloud-info-provider)

The Cloud Information provider generates a representation of cloud resources,
to be published inside INDIGO CMDB.

The generated representation is described using a
[Mako](http://www.makotemplates.org/) template having access to the cloud
middleware information.

## Installation

### Dependencies

The cloud-provider depends on PyYAML and Mako, which are already included as
dependencies for binary packages and when installing from source.

For running the cloud-provider in a production environment, depending on your
setup you will might need for OpenStack to install python-novaclient.

### Binary packages

Packages are available at the [INDIGO repository](http://repo.indigo-datacloud.eu).
Use the appropriate repository for your distribution and install using the usual tools.

### From source

Get the source by cloning this repo and do a pip install.

As pip will have to copy files to /etc/cloud-info-provider-indigo directory,
the user should be able to write to it, so it is recommended to create it
before using pip.

``` sh
sudo mkdir /etc/cloud-info-provider-indigo
sudo chgrp you_user /etc/cloud-info-provider-indigo
sudo chmod g+rwx /etc/cloud-info-provider-indigo
```

``` sh
git clone https://github.com/indigo-dc/cloud-info-provider
cd cloud-info-provider 
pip install .
```
## Configuring the output

Depending on the template used output can range from JSON to LDIF.

The ```--template-extension``` (default: indigo) allows to select different
templates based on thier file extension.
Templates should be available inside the directory ```--template-dir```
(default: /etc/cloud-info-provider-indigo/templates)

The ```--yaml-file``` (default /etc/cloud-info-provider/static.yaml``` allows
to set some static values (see sample.static.yaml for a complete example with comments).

Simple example of /etc/cloud-info-provider/static.yaml:

``` yaml
site:
    name: TEST

compute:
    images:
        defaults:
            # Set to False or comment the line below if you want to show
            # all the images installed in the site (also snapshots). Otherwise
            # only images with a valid marketplace ID (set by the marketplace
            # custom property) are shown
            require_marketplace_id: false
```

Dynamic information can be further obtained with the middleware providers
(OpenStack and OpenNebula supported currently). Use the
`--middleware` option for specifying the provider to use (see the command
help for exact names). cloud-info-provider will fallback to static information
defined in the yaml file if a dynamic provider is not able to return any
information. See the `sample.openstack.yaml` and `sample.opennebula.yaml`
for example configurations for each provider.

Each dynamic provider has its own commandline options for specifying how
to connect to the underlying service. Use the `--help` option for a complete
listing of options.

For example for OpenStack, use a command line similar to the following:
```
cloud-info-provider-indigo-service --middleware openstack \
  --os-username <username> --os-password <password> \
  --os-tenant-name <tenant> --os-auth-url <auth-url>
```

For example for OpenNebula, use a command line similar to the following:
```
cloud-info-provider-indigo-service --middleware indigoon \
  --on-auth <username>:<password> \
  --on-rpcxml-endpoint <rpc-xml-endpoint>
```

Use ```cloud-info-provider-indigo-service --help``` to see the list of available options.

**Test the generation of the output before importing the provider output to the CMDB!**

## Running the provider in a cloud resource middleware

This is the normal deployment mode for the cloud provider. It should be installed
in a node with access to your cloud infrastructure: for OpenStack, access to
nova service is needed; for OpenNebula access to the XML endpoint is required.

## Importing cloud middleware information inside the CMDB.

The provided ```send-to-cmdb``` python script allows to interact with the CMDB 
It will expect JON from its standard input and use CMDB API to import/update
information about images available in the cloud middleware.

``` sh
cloud-info-provider-indigo-service --middleware openstack \
  --os-username <username> --os-password <password> \
  --os-tenant-name <tenant> --os-auth-url <auth-url> 2> /dev/null \
  | send-to-cmdb --cmdb-user <cmdb-user> \
  --cmdb-password <cmdb-password> --sitename <sitename> -v
```

Real example

``` sh
cloud-info-provider-indigo-service --middleware openstack \
  --os-username admin --os-tenant-name demo \
  --os-password openstack \
  --os-auth-url http://192.168.56.101:5000/v2.0 2> /dev/null \
  | send-to-cmdb --cmdb-user cmdb_user --cmdb-password \
  cmdb_password --sitename CYFRONET-CLOUD -v
```

Use ```send-to-cmdb --help``` to see the list of available options.
