%{?scl:%scl_package nodejs-lodash._isiterateecall}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash._isiterateecall

%global npm_name lodash._isiterateecall
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash._isiterateecall
Version:	3.0.9
Release:	3%{?dist}
Summary:	The modern build of lodash’s internal `isIterateeCall` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

%description
The modern build of lodash’s internal `isIterateeCall` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{!?_licensedir:%global license %doc}
%{nodejs_sitelib}/lodash._isiterateecall

%doc README.md
%doc LICENSE.txt

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.9-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.9-2
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.9-1
- Initial build
