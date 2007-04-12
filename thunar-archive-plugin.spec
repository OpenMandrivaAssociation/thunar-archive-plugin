%define __libtoolize /bin/true 

Summary:     An archive plugin for the Thunar File Manager
Name: 		thunar-archive-plugin
Version: 	0.2.4
Release: 	%mkrel 1
License:	GPL
URL: 		http://xfce4-goodies.berlios.de
Source0: 	%{name}-%{version}.tar.bz2
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires:       thunar >= 0.2.2
#optional requires..at least 1 is needed
#Requires:     file-roller
#Requires:     kdeutils-ark
BuildRequires:	thunar-devel >= 0.2.2

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
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS 
%{_libdir}/thunarx-1/*
%{_libdir}/%{name}/*
%{_iconsdir}/hicolor/16x16/apps/tap*


