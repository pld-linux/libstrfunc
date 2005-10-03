#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	libstrfunc - library for manipulating strings
Summary(pl):	libstrfunc - biblioteka do operacji na ³añcuchach znaków
Name:		libstrfunc
Version:	8.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.lionet.info/soft/%{name}-%{version}.tar.gz
# Source0-md5:	f048a3140e811e8eb7d9ca20005ce76a
Patch0:		%{name}-am_no_all_static.patch
URL:		http://www.lionet.info/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Handy library for manipulating strings, string arrays, buffers, CGI
forms, config files et cetera. Handles base64, quoted-printable,
url_encode, mime-words and other encoded data.

%description -l pl
Porêczna biblioteka do operacji na ³añcuchach znaków, tablicach,
buforach, formularzach CGI, plikach konfiguracyjnych itp. Obs³uguje
dane kodowane base64, quoted-printable, url_encode, MIME i w inny
sposób.

%package devel
Summary:	Header files and development documentation for libstrfunc
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libstrfunc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libstrfunc.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libstrfunc.

%package static
Summary:	libstrfunc - static library
Summary(pl):	libstrfunc - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library.

%description static -l pl
Biblioteka statyczna.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--enable-static=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't include "aliases" (copies of base manuals) as they have too common names
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/{[!s],s[!ft],sf[!_],str[!f],strfunc_ctl}*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_mandir}/man3/strfunc.3*
%{_mandir}/man3/sf_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
