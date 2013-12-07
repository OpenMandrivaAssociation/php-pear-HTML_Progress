%define	_class		HTML
%define	_subclass	Progress
%define	modname	%{_class}_%{_subclass}

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear\\(Smarty.class.php\\)'
%else
%define _requires_exceptions	pear(Smarty.class.php)
%endif

Summary:	Including a loading bar in your XHTML documents quickly and easily
Name:		php-pear-%{modname}
Version:	1.2.6
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTML_Progress/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

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

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/ChangeLog
%doc %{modname}-%{version}/INSTALL
%doc %{modname}-%{version}/LICENSE
%doc %{modname}-%{version}/examples
%doc %{modname}-%{version}/Release-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

