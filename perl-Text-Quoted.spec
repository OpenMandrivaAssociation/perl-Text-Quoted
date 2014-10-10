%define upstream_name    Text-Quoted
%define upstream_version 2.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.08
Release:	2

Summary:	Perl module to extract the structure of a quoted mail message
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-Quoted-2.08.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Autoformat)
BuildArch:	noarch

%description
Text::Quoted examines the structure of some text which may contain multiple 
different levels of quoting, and turns the text into a nested data structure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Mar 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.60.0-1mdv2010.1
+ Revision: 521642
- update to 2.06

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.0
+ Revision: 406189
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.05-4mdv2009.0
+ Revision: 258620
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.05-3mdv2009.0
+ Revision: 246639
- rebuild

* Fri Jan 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdv2008.1
+ Revision: 158108
- update to new version 2.05

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2008.1
+ Revision: 108001
- update to new version 2.03
- update to new version 2.03

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.02-1mdv2008.0
+ Revision: 20771
- 2.02


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-4mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 1.8-3mdk
- Do not ship empty dir

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-2mdk
- Fix BuildRequires

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.8-1mdk
- First mandriva package


