#
# cloud-info-provider-service RPM
#

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Information provider for Cloud Compute and Cloud Storage services for INDIGO
Name: cloud-info-provider-indigo
Version: 0.8.2
Release: 1%{?dist}
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/gwarf/cloud-bdii-provider/tree/json_output
Source: cloud_provider_indigo-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-setuptools
BuildRequires: python-pbr
Requires: python
Requires: python-argparse
Requires: python-yaml
Requires: python-mako
Requires: python-requests
#Recommends: bdii
#Recommends: python-novaclient
BuildArch: noarch

%description
Information provider for Cloud Compute and Cloud Storage services for INDIGO
The provider outputs JSON formatted information.
A script allowing to send data to INDIGO CMDB is providred.

%prep
%setup -q -n cloud_provider_indigo-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/cloud_info*
%{python_sitelib}/cloud_provider*
/usr/bin/cloud-info-provider-indigo-service
/usr/bin/send-to-cmdb
%config /etc/cloud-info-provider-indigo/

%changelog
* Tue Aug 02 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.8.2-{%release}
- Fix default value for --yaml-file parameter.
* Fri Jul 29 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.8.1-{%release}
- Add missing dependencies
* Fri Jul 29 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.8.0-{%release}
- Implement deletion of old images once a new one has been uploaded.
* Thu Jul 28 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.7.0-{%release}
- Update mako template
- Add a script for registering images to CMDB
* Wed Jul 27 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.6.1-{%release}
- Update mako template to use fields added by java-syncrepo.
* Wed Jul 6 2016 Baptiste Grenier <baptiste.grenier@egi.eu> - 0.6.0-{%release}
- First release
- Based on cloud-info-provider.spec from EGI-FCTF/cloud-bdii-provider
