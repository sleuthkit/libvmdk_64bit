Name: libvmdk
Version: 20160119
Release: 1
Summary: Library to access the VMware Virtual Disk (VMDK) format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libvmdk/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:               zlib
BuildRequires:               zlib-devel

%description
libvmdk is a library to access the VMware Virtual Disk (VMDK) format

%package devel
Summary: Header files and libraries for developing applications for libvmdk
Group: Development/Libraries
Requires: libvmdk = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libvmdk.

%package tools
Summary: Several tools for accessing VMware Virtual Disk (VMDK) files
Group: Applications/System
Requires: libvmdk = %{version}-%{release} fuse-libs
BuildRequires: fuse-devel

%description tools
Several tools for accessing VMware Virtual Disk (VMDK) files

%package python
Summary: Python 2 bindings for libvmdk
Group: System Environment/Libraries
Requires: libvmdk = %{version}-%{release} python
BuildRequires: python-devel

%description python
Python 2 bindings for libvmdk

%package python3
Summary: Python 3 bindings for libvmdk
Group: System Environment/Libraries
Requires: libvmdk = %{version}-%{release} python3
BuildRequires: python3-devel

%description python3
Python 3 bindings for libvmdk

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvmdk.pc
%{_includedir}/*
%{_mandir}/man3/*

%files tools
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/vmdkinfo
%attr(755,root,root) %{_bindir}/vmdkmount
%{_mandir}/man1/*

%files python
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files python3
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%changelog
* Tue Jan 19 2016 Joachim Metz <joachim.metz@gmail.com> 20160119-1
- Auto-generated

