#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Vector and Matrix Math Library for C++
Summary(pl.UTF-8):	Vector and Matrix Math Library - biblioteka matematyczna wektorów i macierzy w C++
Name:		vmmlib
Version:	1.10.0
Release:	1
License:	BSD
Group:		Libraries
# latest is 1.6.2 here
#Source0:	https://github.com/VMML/vmmlib/archive/release-%{version}/%{name}-%{version}.tar.gz
# use Eyescale version for now
Source0:	https://github.com/Eyescale/vmmlib/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6d1c7c3f8db8f730367cf0a4401bd8a0
URL:		http://vmml.github.io/vmmlib/
BuildRequires:	Eyescale-CMake >= 2016.04
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
%setup -q

ln -s %{_datadir}/Eyescale-CMake CMake/common
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

%{__rm} $RPM_BUILD_ROOT%{_datadir}/vmmlib/{ACKNOWLEDGEMENTS,LICENSE.txt,README.md}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vmmlib/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS LICENSE.txt README.md doc/Changelog.md
%{_includedir}/vmmlib
%dir %{_datadir}/vmmlib
%{_datadir}/vmmlib/CMake

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
%endif
