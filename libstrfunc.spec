Summary:	libstrfunc - library for manipulating strings
Summary(pl):	libstrfunc - biblioteka do manipulowania stringami
Name:		libstrfunc
Version:	7.1.0
Release:	1
License:	BSD like
Group:		Applications/System
Source0:	http://www.spelio.net.ru/soft/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
URL:		http://www.spelio.net.ru/soft/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Handy library for manipulating strings, string arrays, buffers, CGI
forms, config files et cetera. Handles base64, quoted-printable,
url_encode, mime-words and other encoded data.

%description -l pl
Porêczna biblioteka do manipulowania stringami, tablicami, buforami,
formularzami CGI, plikami konfiguracyjnymi et cetera.

%package devel
Summary:	Header files and development documentation for libstrfunc
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libstrfunc
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libstrfunc.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libstrfunc.

%package static
Summary:	libstrfunc - static library
Summary(pl):	libstrfunc - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static library.

%description static -l pl
Biblioteka statyczna.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS COPYRIGHT ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
