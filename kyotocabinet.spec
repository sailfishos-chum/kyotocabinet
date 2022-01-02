Summary: Kyoto Cabinet is a library of routines for managing a database
Name: libkyotocabinet
Version: 1.2.77
Release: 1%{?dist}
License: LGPL and BSD 2-clause license
Group: Development/Libraries
URL: http://fallabs.com/kyotocabinet

Source: http://fallabs.com/kyotocabinet/pkg/kyotocabinet-%{version}.tar.gz
Patch0:     rm_native_optimization.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: zlib
BuildRequires: gcc-c++ zlib-devel

%description
Kyoto Cabinet is a library of routines for managing a
database. The database is a simple data file containing records, each
is a pair of a key and a value. Every key and value is serial bytes
with variable length. Both binary data and character string can be
used as a key and a value. Each key must be unique within a
database. There is neither concept of data tables nor data
types. Records are organized in hash table or B+ tree.

PackageName: Kyoto Cabinet
Categories:
  - Library

%package devel
Summary: Kyoto Cabinet development headers and static library
Group: Development/Libraries
#Requires: %{name} = %{version}

%description devel
Kyoto Cabinet is a library of routines for managing a
database. Development package

PackageName: Kyoto Cabinet Development
Categories:
  - Library

%package tools
Summary: Kyoto Cabinet tools
Group: Libraries/Databases
Requires: %{name} = %{version}

%description tools
Kyoto Cabinet is a library of routines for managing a
database. Test tools

PackageName: Kyoto Cabinet Tools
Type: console-application
Categories:
  - Utility

%prep
%setup -q -n kyotocabinet-%{version}
%patch0 -p1

%build
%{__make} clean || true

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure 

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n libkyotocabinet -p /sbin/ldconfig

%postun -n libkyotocabinet -p /sbin/ldconfig

%files
%files
%defattr(-, root, root, 0755)
%{_libdir}/libkyotocabinet.so.16.13.0
%{_libdir}/libkyotocabinet.so.16
%{_libdir}/libkyotocabinet.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kc*.h
%{_libdir}/libkyotocabinet.a
%{_libdir}/pkgconfig/kyotocabinet.pc

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/kc*
%{_mandir}/man1/kc*
%{_defaultdocdir}/kyotocabinet

%changelog
* Thu Mar 23 2017 rinigus <rinigus.git@gmail.com> - 1.2.76
- initial packaging release for SFOS
