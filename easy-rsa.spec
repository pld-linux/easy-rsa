Summary:	Small RSA key management package
Summary(pl.UTF-8):	Mały pakiet do zarządzania kluczami RSA
Name:		easy-rsa
Version:	2.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://build.openvpn.net/downloads/releases/%{name}-%{version}_master.tar.gz
# Source0-md5:	fbf818b6e1f212e77b9ce0e6d92584a1
Patch0:		%{name}2.patch
URL:		http://openvpn.net/easyrsa.html
Requires:	grep
Requires:	openssl-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small RSA key management package, based on the openssl
command line tool, that can be found in the easy-rsa subdirectory of
the OpenVPN distribution. While this tool is primary concerned with
key management for the SSL VPN application space, it can also be used
for building web certificates.

%description -l pl.UTF-8
To jest mały pakiet do zarządzania kluczami RSA, oparty na narzędziu
linii poleceń openssl. Pakiet ten pochodzi z podkatalogu easy-rsa
dystrybucji OpenVPN.

%prep
%setup -q -n %{name}-%{version}_master
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}/easy-rsa/keys}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

mv $RPM_BUILD_ROOT%{_datadir}/easy-rsa/openssl-1.0.0.cnf $RPM_BUILD_ROOT%{_sysconfdir}/easy-rsa/openssl.cnf
rm $RPM_BUILD_ROOT%{_datadir}/easy-rsa/openssl-*.cnf
mv $RPM_BUILD_ROOT%{_datadir}/easy-rsa/vars $RPM_BUILD_ROOT%{_sysconfdir}/easy-rsa/
mv $RPM_BUILD_ROOT%{_datadir}/easy-rsa/pkitool $RPM_BUILD_ROOT%{_sbindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README-2.0
%dir %{_sysconfdir}/easy-rsa
%attr(700,root,root) %dir %{_sysconfdir}/easy-rsa/keys
%config(noreplace) %attr(640,root,root) %verify(not md5 mtime size) %{_sysconfdir}/easy-rsa/vars
%config(noreplace) %attr(640,root,root) %verify(not md5 mtime size) %{_sysconfdir}/easy-rsa/openssl.cnf
%attr(755,root,root) %{_sbindir}/pkitool
%dir %{_datadir}/easy-rsa
%attr(755,root,root) %{_datadir}/easy-rsa/*
