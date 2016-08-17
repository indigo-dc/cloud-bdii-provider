# Developer documentation

## Building from source

Get the source by cloning this repo and do a pip install.

As pip will have to copy files to /etc/cloud-info-provider-indigo directory,
the installation user should be able to write to it, so it is recommended to
create it before using pip.

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

## Buliding package on Ubuntu

``` sh
sudo apt install devscripts build-essential debhelper python-all python-all-dev python-pbr python-setuptools python-support
debuild --no-tgz-check binary
```

## Building package on CentOS

``` sh
sudo yum install rpm-build python-br
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
mkdir -p ~/rpmbuild/SOURCES
python setup.py sdist
cp dist/cloud_provider_indigo-*.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba rpm/cloud-info-provider-indigo.spec
```
