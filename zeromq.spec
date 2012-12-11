%define name	zeromq
%define version	3.2.0
%define release 0.1

%define libname_orig lib%{name} 
%define major	3
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Software library for fast, message-based applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://download.zeromq.org/%{name}-%{version}-rc1.tar.gz
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
export CFLAGS="$CFLAGS -fno-strict-aliasing -Wno-error=unused-variable" CXXFLAGS="$CXXFLAGS -Wno-error=unused-variable"
./configure --prefix=/usr --with-pgm
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/libzmq.so.%{major}*

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



%changelog
* Tue Sep 18 2012 Crispin Boylan <crisb@mandriva.org> 3.2.0-0.1
+ Revision: 817102
- Update to 3.2.0-rc1

* Wed Apr 04 2012 Lev Givon <lev@mandriva.org> 2.2.0-1
+ Revision: 789199
- Update to 2.2.0.

* Tue Dec 20 2011 Guilherme Moro <guilherme@mandriva.com> 2.1.11-2
+ Revision: 743986
- enable openpgm support

* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 2.1.11-1
+ Revision: 743652
- Update to 2.1.11.

* Mon Oct 03 2011 Lev Givon <lev@mandriva.org> 2.1.10-1
+ Revision: 702574
- Update to 2.1.10.

* Mon Aug 29 2011 Lev Givon <lev@mandriva.org> 2.1.9-1
+ Revision: 697394
- Update to 2.1.9.

* Thu Jul 28 2011 Lev Givon <lev@mandriva.org> 2.1.8-1
+ Revision: 692074
- Update to 2.1.8.

* Thu May 12 2011 Lev Givon <lev@mandriva.org> 2.1.7-1
+ Revision: 673876
- Update to 2.1.7.

* Wed Apr 27 2011 Lev Givon <lev@mandriva.org> 2.1.6-1
+ Revision: 659697
- Update to 2.1.6.

* Wed Mar 30 2011 Lev Givon <lev@mandriva.org> 2.1.4-1
+ Revision: 649232
- Update to 2.1.4.

* Thu Mar 24 2011 Lev Givon <lev@mandriva.org> 2.1.3-2
+ Revision: 648351
- Make lib package obsolete zeromq-utils.

* Thu Mar 24 2011 Lev Givon <lev@mandriva.org> 2.1.3-1
+ Revision: 648186
- Update to 2.1.3.
  Don't build PGM extension.

* Sun Mar 06 2011 Lev Givon <lev@mandriva.org> 2.1.2-0.rc2.0
+ Revision: 642270
- Update to 2.1.2 rc2.

* Wed Feb 23 2011 Lev Givon <lev@mandriva.org> 2.1.1-0.rc1.1
+ Revision: 639473
- Python required to build the PGM extension.

* Wed Feb 23 2011 Lev Givon <lev@mandriva.org> 2.1.1-0.rc1.0
+ Revision: 639459
- Update to 2.1.1 rc1.
  Build with PGM support.

* Mon Feb 07 2011 Lev Givon <lev@mandriva.org> 2.1.0-0.beta.0
+ Revision: 636698
- Update to 2.1.0 beta.

* Tue Nov 02 2010 Lev Givon <lev@mandriva.org> 2.0.10-1mdv2011.0
+ Revision: 592249
- import zeromq

