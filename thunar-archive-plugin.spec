Summary:	An archive plugin for the Thunar File Manager
Name:		thunar-archive-plugin
Version:	0.2.4
Release: 	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://foo-projects.org/~benny/projects/thunar-archive-plugin
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel >= 0.8.0
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

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS 
%{_libdir}/thunarx-1/*
%{_libdir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
