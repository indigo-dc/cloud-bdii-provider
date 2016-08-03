# Developer documentation

## Building from source

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
