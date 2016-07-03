#
# cloud-info-provider-service RPM
#

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Information provider for Cloud Compute and Cloud Storage services for INDIGO
Name: cloud-info-provider-indigo
Version: 0.6
Release: 1%{?dist}
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/gwarf/cloud-bdii-provider/tree/json_output
Source: cloud-info-provider-indigo-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-setuptools
BuildRequires: python-pbr
Requires: python
Requires: python-argparse
Requires: python-yaml
#Recommends: bdii
#Recommends: python-novaclient
BuildArch: noarch

%description
Information provider for Cloud Compute and Cloud Storage services for INDIGO
The provider outputs JSON formatted information.

%prep
%setup -q -n cloud-bdii-provider-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/cloud_bdii*
%{python_sitelib}/cloud_provider*
/usr/bin/cloud-info-provider-indigo-service
%config /etc/cloud-info-provider-indigo/

%changelog
* Wed Jul 6 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.1-{%release}
- First release
- Based on cloud-info-provider.spec from EGI-FCTF/cloud-bdii-provider
