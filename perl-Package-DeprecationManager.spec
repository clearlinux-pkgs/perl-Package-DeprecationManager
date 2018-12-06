#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-DeprecationManager
Version  : 0.17
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Package-DeprecationManager-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Package-DeprecationManager-0.17.tar.gz
Summary  : 'Manage deprecation warnings for your distribution'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Package-DeprecationManager-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)

%description
# NAME
Package::DeprecationManager - Manage deprecation warnings for your distribution

%package dev
Summary: dev components for the perl-Package-DeprecationManager package.
Group: Development
Provides: perl-Package-DeprecationManager-devel = %{version}-%{release}

%description dev
dev components for the perl-Package-DeprecationManager package.


%package license
Summary: license components for the perl-Package-DeprecationManager package.
Group: Default

%description license
license components for the perl-Package-DeprecationManager package.


%prep
%setup -q -n Package-DeprecationManager-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-DeprecationManager
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-DeprecationManager/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Package/DeprecationManager.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::DeprecationManager.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-DeprecationManager/LICENSE
