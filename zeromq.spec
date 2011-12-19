%define name	zeromq
%define version	2.1.11
%define release %mkrel 1

%define libname_orig lib%{name} 
%define major	1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Software library for fast, message-based applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
License:	LGPLv3+
Group:		Development/Other
Url:		http://www.zeromq.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	libuuid-devel
BuildRequires:	python

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
Obsoletes:	%{name}-utils

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

%prep
%setup -q

%build
export CFLAGS="$CFLAGS -fno-strict-aliasing"
./configure --prefix=/usr
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
%if %mdkversion < 201200
%{_libdir}/libzmq.la
%endif
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*

