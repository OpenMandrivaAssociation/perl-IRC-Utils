%define upstream_name    IRC-Utils
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Common utilities for IRC-related tasks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IRC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The functions in this module take care of many of the tasks you are faced
with when working with IRC. Mode lines, ban masks, message encoding and
formatting, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Fri Aug 12 2011 Michael Scherer <misc@mandriva.org> 0.110.0-1mdv2012.0
+ Revision: 694074
- new version

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1
+ Revision: 682132
- update to new version 0.10

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 677370
- update to new version 0.09

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 673799
- update to new version 0.08

* Sun May 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1
+ Revision: 661392
- import perl-IRC-Utils

