%define		_class		HTML
%define		_subclass	Progress
%define		upstream_name	%{_class}_%{_subclass}

%define _requires_exceptions	pear(Smarty.class.php)

Name:		php-pear-%{upstream_name}
Version:	1.2.6
Release:	%mkrel 6
Summary:	Including a loading bar in your XHTML documents quickly and easily
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Progress/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides a way to add a loading bar fully costomizable in
existing XHTML documents.

Your browser should accept DHTML feature.

Features:
- allows usage of an existing stylesheet for colors and size model
- all colors and size elements are customizable
- show or hide text percent information
- set/add and returns value of current status of progress
- compliant with all CSS/XHTML standards
- integration with template engine ITx family is possible
- create horizontal and also vertical bart
- optional message line come with progress status
- percent info is floating all around the progress bar
- scale can be changed (default is 100)
- legend of percent text info can be changed (default is "%")

This class has in PEAR status: %{_status}.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog
%doc %{upstream_name}-%{version}/INSTALL
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/Release-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
