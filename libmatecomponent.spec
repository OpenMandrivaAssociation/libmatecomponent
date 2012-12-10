%define major		0
%define act_major	4
%define libname		%mklibname matecomponent %{major}
%define libactivation	%mklibname matecomponent-activation %{act_major}
%define develname	%mklibname matecomponent -d

Summary:	A fork of GNOME libbonobo
Name:		libmatecomponent
Version:	1.4.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(MateCORBA-2.0)
BuildRequires:	pkgconfig(popt)

%description
libmatecomponent is a fork of GNOME libbonobo.

libmatecomponent is the non-GUI part of the matecomponent component
infrastructure, it is most useful for creating aggregate interfaces & doing
IPC easily. It also contains a rather badly designed & implemented per-system
activation system. This needs re-writing & simplifying to be per-display.

%package -n %{libname}
Summary:	A fork of GNOME libbonobo
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{libactivation}
Summary:	A fork of GNOME libbonobo
Group:		System/Libraries

%description -n %{libactivation}
This package contains the shared library for %{name}.

%package -n %{develname}
Summary:        A fork of GNOME libbonobo
Group:          Development/C
Requires:	%{libname} = %{version}
Requires:	%{libactivation} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{develname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%dir %{_sysconfdir}/matecomponent-activation
%{_sysconfdir}/matecomponent-activation/matecomponent-activation-config.xml
%{_sbindir}/matecomponent-activation-sysconf
%{_bindir}/matecomponent-activation-client
%{_bindir}/matecomponent-slay
%{_bindir}/matecomponent-activation-run-query
%{_bindir}/matecomponent-echo-client-2
%dir %{_libdir}/matecorba-2.0
%{_libdir}/matecorba-2.0/MateComponent_module.so
%{_libdir}/matecomponent-activation-server
%dir %{_libdir}/matecomponent
%{_libdir}/matecomponent/monikers/libmoniker_std_2.so
%{_libdir}/matecomponent/servers/MateComponent_Moniker_std.server
%{_libdir}/matecomponent/servers/MateComponent_CosNaming_NamingContext.server
%{_libdir}/matecomponent/servers/MateComponent_Sample_Echo.server
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmatecomponent-2.so.%{major}*

%files -n %{libactivation}
%{_libdir}/libmatecomponent-activation.so.%{act_major}*

%files -n %{develname}
%{_libdir}/libmatecomponent-activation.so
%{_libdir}/libmatecomponent-2.so
%{_libdir}/pkgconfig/matecomponent-activation-2.0.pc
%{_libdir}/pkgconfig/libmatecomponent-2.0.pc
%dir %{_libdir}/matecomponent-2.0
%{_libdir}/matecomponent-2.0/samples/matecomponent-echo-2
%dir %{_includedir}/matecomponent-activation-2.0
%{_includedir}/matecomponent-activation-2.0/matecomponent-activation/*
%dir %{_includedir}/libmatecomponent-2.0
%{_includedir}/libmatecomponent-2.0/*
%dir %{_datadir}/idl
%{_datadir}/idl/*
%dir %{_datadir}/gtk-doc/html/matecomponent-activation
%{_datadir}/gtk-doc/html/matecomponent-activation/*
%dir %{_datadir}/gtk-doc/html/libmatecomponent
%{_datadir}/gtk-doc/html/libmatecomponent/*


%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811336
- new version 1.4.0

* Tue May 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.1-1
+ Revision: 801126
- imported package libmatecomponent

