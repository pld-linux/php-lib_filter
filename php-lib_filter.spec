%define		php_min_version 5.0.0
%define		pkgname	lib_filter
%include	/usr/lib/rpm/macros.php
Summary:	An HTML filtering library in PHP
Name:		php-%{pkgname}
Version:	1.15
Release:	0.1
License:	CC by sa 2.5
Group:		Development/Languages/PHP
Source0:	http://code.iamcal.com/php/lib_filter/lib_filter_r%{version}.zip
# Source0-md5:	bb5e977e6293fcc8988b6437135ab554
URL:		http://iamcal.com/publish/articles/php/processing_html/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML filtering library in PHP.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a lib_filter.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/lib_filter.php
