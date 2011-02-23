%define name	zeromq
%define version	2.1.1
%define release %mkrel 0.rc1.0

%define libname_orig lib%{name} 
%define major	1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Software library for fast, message-based applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.zeromq.org/local--files/area:download/%{name}-%{version}.tar.gz
License:	LGPLv3+
Group:		Development/Other
Url:		http://www.zeromq.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	libuuid-devel

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package -n	%{libname}
Summary: 	Software library for fast, message-based applications
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ${name} shared library.

%package -n	%{develname}
Summary: 	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{develname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the libraries and header files needed to develop
applications that use %{name}.

%package -n	%{name}-utils
Summary: 	Utilities for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n %{name}-utils
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains %{name}-related utilities.

%prep
%setup -q

%build
%ifarch pentium3 pentium4 athlon i386 i486 i586 i686 x86_64
%configure2_5x --with-pgm
%else
%configure2_5x
%endif
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/libzmq.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libzmq.a
%{_libdir}/libzmq.la
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*

%files -n %{name}-utils
%defattr(-,root,root)
%{_bindir}/zmq*
%{_mandir}/man1/zmq*
