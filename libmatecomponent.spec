%define major		0
%define libname		%mklibname matecomponent %{major}
%define develname	%mklibname matecomponent -d

Name:		libmatecomponent
Summary:	A fork of GNOME libbonobo
Version:	1.2.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
BuildRequires:	mate-common
BuildRequires:	mate-corba-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	pkgconfig(popt) >= 1.5
BuildRequires:	intltool >= 0.25
BuildRequires:	gtk-doc >= 1.0

%description
libmatecomponent is a fork of GNOME libbonobo.

libmatecomponent is the non-GUI part of the matecomponent component
infrastructure, it is most useful for creating aggregate interfaces & doing
IPC easily. It also contains a rather badly designed & implemented per-system
activation system. This needs re-writing & simplifying to be per-display.

%package -n ${libname}
Summary:	A fork of GNOME libbonobo
Group:		System/Libraries

%description -n ${libname}
libmatecomponent is a fork of GNOME libbonobo.

libmatecomponent is the non-GUI part of the matecomponent component
infrastructure, it is most useful for creating aggregate interfaces & doing
IPC easily. It also contains a rather badly designed & implemented per-system
activation system. This needs re-writing & simplifying to be per-display.

%package -n ${develname}
Summary:        A fork of GNOME libbonobo
Group:          Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n ${develname}
libmatecomponent is a fork of GNOME libbonobo.

libmatecomponent is the non-GUI part of the matecomponent component
infrastructure, it is most useful for creating aggregate interfaces & doing
IPC easily. It also contains a rather badly designed & implemented per-system
activation system. This needs re-writing & simplifying to be per-display.

%prep
%setup -q

%build
%setup_compile_flags
./autogen.sh \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--disable-static \
	--libexecdir=%{_libexecdir}
make

%install
%makeinstall_std

%files

