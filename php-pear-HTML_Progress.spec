%define		_class		HTML
%define		_subclass	Progress
%define		upstream_name	%{_class}_%{_subclass}

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear\\(Smarty.class.php\\)'
%else
%define _requires_exceptions	pear(Smarty.class.php)
%endif

Name:		php-pear-%{upstream_name}
Version:	1.2.6
Release:	10
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



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog
%doc %{upstream_name}-%{version}/INSTALL
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/Release-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-7mdv2011.0
+ Revision: 667503
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-6mdv2011.0
+ Revision: 607104
- rebuild

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.6-5mdv2010.1
+ Revision: 478091
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.6-4mdv2010.0
+ Revision: 399772
- spec cleanup
- don't duplicate spec-helper job
- fix bogus dependency

* Fri Jul 24 2009 Raphaël Gertz <rapsys@mandriva.org> 1.2.6-3mdv2010.0
+ Revision: 399533
- Rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-2mdv2009.1
+ Revision: 321833
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdv2009.0
+ Revision: 272586
- 1.2.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-5mdv2009.0
+ Revision: 224739
- rebuild

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-4mdv2008.1
+ Revision: 166132
- rpmlint fixes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-3mdv2008.0
+ Revision: 15455
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-2mdv2007.0
+ Revision: 81099
- Import php-pear-HTML_Progress

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-1mdk
- 1.2.5

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdk
- rule out some auto deps

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- 1.2.3

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- 1.2.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (PLD import)

