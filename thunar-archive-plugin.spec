%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	An archive plugin for the Thunar File Manager
Name:		thunar-archive-plugin
Version:	0.5.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/thunar-plugins/thunar-archive-plugin
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-archive-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	xfce4-dev-tools

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
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%{_libdir}/thunarx-3/*
%{_libexecdir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
