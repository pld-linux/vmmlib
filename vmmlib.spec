#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Vector and Matrix Math Library for C++
Summary(pl.UTF-8):	Vector and Matrix Math Library - biblioteka matematyczna wektorów i macierzy w C++
Name:		vmmlib
Version:	1.14.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/Eyescale/vmmlib/releases
Source0:	https://github.com/Eyescale/vmmlib/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f25e57bfc1e4699447963f5dbafd22f2
URL:		http://vmml.github.io/vmmlib/
BuildRequires:	Eyescale-CMake >= 2018.02
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.1
%{?with_apidocs:BuildRequires:	doxygen}
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for vmmlib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki vmmlib.

%prep
%setup -q

rmdir CMake/common
ln -s %{_datadir}/Eyescale-CMake CMake/common

%build
install -d build
cd build
%cmake ..
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
