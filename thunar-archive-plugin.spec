%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	An archive plugin for the Thunar File Manager
Name:		thunar-archive-plugin
Version:	0.3.0
Release: 	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-archive-plugin
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-archive-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel >= 1.2.0
BuildRequires:	intltool
BuildRequires:	exo-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The thunar-archive-plugin is a plugin for the Thunar File Manager, which
adds archive operations to the file context menus. Using this plugin you
will be able to extract and create archive files from within Thunar using
a single click.
The plugin now supports a variety of archive managers through a generic
interface, that requires the archive manager to install a .desktop file
as usual, that lists the supported mime types, and a .tap file that acts
as a wrapper script to invoke the archive manager with the appropriate
parameters for the create, extract-here and extract-to actions.
Wrapper scripts for file-roller (the GNOME archive manager) and ark (the
KDE archive manager) have been added. Xarchiver, the Xfce archive manager,
will include an appropriate xarchiver.tap file in the next release. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_libdir}/thunarx-2/*
%{_libdir}/%{name}
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 632819
- add buildrequires on exo-devel
- add buildrequires on intltool
- update to new version 0.3.0
- update url for Source0
- drop old scriplets

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-9mdv2010.1
+ Revision: 543281
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2.4-8mdv2010.0
+ Revision: 445421
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-7mdv2009.1
+ Revision: 349181
- rebuild whole xfce

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-6mdv2009.1
+ Revision: 294885
- rebuild for new Thunar  (Xfce4.6 beta1)

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-5mdv2009.0
+ Revision: 219663
- run scriplets only for mdv older than 2009

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-4mdv2009.0
+ Revision: 219406
- fix file list

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.4-4mdv2008.1
+ Revision: 170641
- remove require on empty package that no more exists
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-3mdv2008.1
+ Revision: 110827
- do not package COPYING and INSTALL files
- be more explicit on thunar-devel version

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.4-2mdv2008.0
+ Revision: 33277
- spec file clean
- add macros to %%post and %%postun


* Mon Feb 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.2.4-1mdv2007.0
+ Revision: 116280
- New release 0.2.4
- New release 0.2.2
- Import thunar-archive-plugin

* Wed Jul 05 2006 Charles A Edwards <eslrahc@mandriva.org> 0.2.0-1mdv2007.0
- 0.2.0
- rm explicit R for file-roller
- update file list

* Sat Jun 24 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1.2-1mdv2007.0
- initial mandriva package

