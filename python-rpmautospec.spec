%global srcname rpmautospec

Name:           python-rpmautospec
Version:        0.0.1
Release:        1%{?dist}
Summary:        Provides a cli tool and a library for autorel and autochangelog

License:        MIT
URL:            https://pagure.io/Fedora-Infra/rpmautospec
Source0:        rpmautospec-0.0.1.tar.gz

BuildArch:      noarch

%global _description %{expand:
Provides a cli tool and koji plugin for autorel and autochangelog
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  koji
%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3-rpm
Requires: python3-koji
Requires: python3-pygit2

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
#install -m 0644 koji_plugin/rpmautospec_plugin.py %{buildroot}/usr/lib/koji-hub-plugins/

#%package -n rpmautospec-koji-plugin
#Summary: Provides the koji plugin for autorel and autochangelog
#Requires: python3-%{srcname} == %{version}-%{release}
#Requires: koji

#%description -n rpmautospec-koji-plugin 
#Provides the koji plugin for autorel and autochangelog

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/
%{_bindir}/rpmautospec.py

%files -n rpmautospec-koji-plugin
%{buildroot}/usr/lib/koji-hub-plugins/rpmautospec_plugin.py

%changelog
* Wed Mar 18 2020  Adam Saleh <asaleh@redhat.com> - 0.0.1-1
- initial package for Fedora
