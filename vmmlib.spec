#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Vector and Matrix Math Library for C++
Summary(pl.UTF-8):	Vector and Matrix Math Library - biblioteka matematyczna wektorów i macierzy w C++
Name:		vmmlib
Version:	1.8.0
Release:	1
License:	BSD
Group:		Libraries
# latest is 1.6.2 here
#Source0:	https://github.com/VMML/vmmlib/archive/release-%{version}/%{name}-%{version}.tar.gz
# use Eyescale version for now
Source0:	https://github.com/Eyescale/vmmlib/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	66fcb200c33a1bc95eb7db1de4933655
Source1:	https://github.com/Eyescale/CMake/archive/139ce7d/Eyescale-CMake-139ce7d.tar.gz
# Source1-md5:	4a6abcd9e0fc417528a8ca68a97e65eb
URL:		http://vmml.github.io/vmmlib/
BuildRequires:	blas-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
Requires:	boost-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A templatized C++ vector and matrix math library.

%description -l pl.UTF-8
Biblioteka matematyczna wektorów i macierzy oparta na szablonach C++.

%package apidocs
Summary:	vmmlib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki vmmlib
Group:		Documentation

%description apidocs
API documentation for vmmlib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki vmmlib.

%prep
%setup -q -a1

%{__mv} CMake-* CMake/common
%{__rm} .gitexternals

%build
install -d build
cd build
%cmake .. \
	-DBUILDYARD_DISABLED=ON
%{__make}

%if %{with apidocs}
doxygen doc/Doxyfile
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/vmmlib/{ACKNOWLEDGEMENTS,AUTHORS,LICENSE.txt,README.md}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vmmlib/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS CHANGES LICENSE.txt README.md doc/RELNOTES.md
%{_includedir}/vmmlib
%{_pkgconfigdir}/vmmlib.pc
%dir %{_datadir}/vmmlib
%{_datadir}/vmmlib/CMake

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
%endif
