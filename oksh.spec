Name:   oksh
Version:        0.5.0
Release:        1%{?dist}
Summary:        OpenBSD KSH for RHEL 6

Group:          Applications/Shells
License:        BSD
URL:            http://www.connochaetos.org/oksh/
Distribution:   chstuff
Vendor:         gwurr3
Packager:       Glenn Wurr III <glenn@wurr.net>
Source0:        http://www.connochaetos.org/oksh/oksh-0.5.0.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/oksh-XXXXXX)

BuildRequires:  gcc

Requires:       bash

%description
A package of OpenBSD's KSH ported to Linux

%prep
%setup -q


%build

./configure --prefix=/ --exec-prefix=/usr

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install bindir=%{buildroot}/bin mandir=%{buildroot}/usr/man/man1


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%verify(mode md5 size mtime) /bin/ksh
%verify(mode md5 size mtime) /usr/man/*


%changelog

* Sun Sep 28 2015 Glenn Wurr III <glenn@wurr.net> 0.5.0-1-
First Build

%post
echo "/bin/ksh" >> /etc/shells

%postun
sed -i '/ksh/d' /etc/shells
