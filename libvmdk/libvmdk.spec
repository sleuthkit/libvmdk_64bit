Name: libvmdk
Version: 20200810
Release: 1
Summary: Library to access the VMware Virtual Disk (VMDK) format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libvmdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:              zlib
BuildRequires: gcc              zlib-devel

%description -n libvmdk
Library to access the VMware Virtual Disk (VMDK) format

%package -n libvmdk-static
Summary: Library to access the VMware Virtual Disk (VMDK) format
Group: Development/Libraries
Requires: libvmdk = %{version}-%{release}

%description -n libvmdk-static
Static library version of libvmdk.

%package -n libvmdk-devel
Summary: Header files and libraries for developing applications for libvmdk
Group: Development/Libraries
Requires: libvmdk = %{version}-%{release}

%description -n libvmdk-devel
Header files and libraries for developing applications for libvmdk.

%package -n libvmdk-python2
Obsoletes: libvmdk-python < %{version}
Provides: libvmdk-python = %{version}
Summary: Python 2 bindings for libvmdk
Group: System Environment/Libraries
Requires: libvmdk = %{version}-%{release} python2
BuildRequires: python2-devel

%description -n libvmdk-python2
Python 2 bindings for libvmdk

%package -n libvmdk-python3
Summary: Python 3 bindings for libvmdk
Group: System Environment/Libraries
Requires: libvmdk = %{version}-%{release} python3
BuildRequires: python3-devel

%description -n libvmdk-python3
Python 3 bindings for libvmdk

%package -n libvmdk-tools
Summary: Several tools for reading VMware Virtual Disk (VMDK) files
Group: Applications/System
Requires: libvmdk = %{version}-%{release} fuse-libs
BuildRequires: fuse-devel

%description -n libvmdk-tools
Several tools for reading VMware Virtual Disk (VMDK) files

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

%files -n libvmdk
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libvmdk-static
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.a

%files -n libvmdk-devel
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvmdk.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libvmdk-python2
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files -n libvmdk-python3
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%files -n libvmdk-tools
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Aug 10 2020 Joachim Metz <joachim.metz@gmail.com> 20200810-1
- Auto-generated

