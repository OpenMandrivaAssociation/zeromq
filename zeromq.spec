%define major 3
%define oldlib %mklibname %{name} %{major}
%define olddev %mklibname %{name} -d
%define oname zmq
%define libname %mklibname %{oname} %{major}
%define devname %mklibname %{oname} -d

Summary:	Software library for fast, message-based applications
Name:		zeromq
Version:	3.2.4
Release:	4
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
Patch0:		zeromq-3.2.4-fix-strict-aliasing-violations.patch
License:	LGPLv3+
Group:		Development/Other
Url:		http://www.zeromq.org
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(openpgm-5.2)
BuildRequires:	python

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package -n	%{libname}
Summary:	Software library for fast, message-based applications
Group:		System/Libraries
Obsoletes:	%{name}-utils
%rename		%{oldlib}

%description -n %{libname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the %{name} shared library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{olddev}

%description -n %{devname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the libraries and header files needed to develop
applications that use %{name}.

%prep
%setup -q 
%patch0 -p1 -b .aliasing~
autoreconf -fiv

%build
%configure --with-system-pgm
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libzmq.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*
