%define realname   Text-Quoted

Name:		perl-%{realname}
Version:    2.05
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl module to extract the structure of a quoted mail message
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl(Text::Autoformat)
BuildArch: noarch

%description
Text::Quoted examines the structure of some text which may contain multiple 
different levels of quoting, and turns the text into a nested data structure.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

