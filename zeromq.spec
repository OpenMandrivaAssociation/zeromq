%define major 5
%define oldlibname %mklibname zmq 5
%define libname %mklibname zmq
%define devname %mklibname zmq -d
%define beta %nil

Summary:	Software library for fast, message-based applications
Name:		zeromq
Version:	4.3.5
%if "%{beta}" != ""
Release:	0.%{beta}.1
Source0:	http://download.zeromq.org/%{name}-%{version}-%{beta}.tar.gz
%else
Release:	1
Source0:	https://github.com/zeromq/libzmq/releases/download/v%{version}/zeromq-%{version}.tar.gz
%endif
License:	LGPLv3+
Group:		Development/Other
Url:		https://www.zeromq.org
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(openpgm-5.2)
BuildRequires:	pkgconfig(libsodium)
BuildRequires:	python
# For man page generation
BuildRequires:	xmlto asciidoc
BuildSystem:	autotools
BuildOption:	--with-system-pgm
BuildOption:	--with-libsodium

%patchlist
zeromq-4.3.5-clang.patch

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package -n %{libname}
Summary:	Software library for fast, message-based applications
Group:		System/Libraries
Obsoletes:	%{name}-utils
%rename %{oldlibname}

%description -n %{libname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the %{name} shared library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
%rename		%{_lib}zeromq-devel

%description -n %{devname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the libraries and header files needed to develop
applications that use %{name}.

#CXXFLAGS="%{optflags} -Wno-error=gnu-statement-expression"

%files -n %{libname}
%{_libdir}/libzmq.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS
%{_bindir}/curve_keygen
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*
