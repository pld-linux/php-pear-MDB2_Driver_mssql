%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_mssql
%define		_status		beta
%define		_pearname	MDB2_Driver_mssql
%define		subver	b3
%define		rel		3
Summary:	%{_pearname} - mssql MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik mssql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	9215b90b0597a56357552d8407e04232
URL:		http://pear.php.net/package/MDB2_Driver_mssql/
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(mssql)
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b3
Obsoletes:	php-pear-MDB2_Driver_mssql-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Microsoft SQL Server MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik Microsoft SQL Server dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/mssql.php
%{php_pear_dir}/MDB2/Driver/Manager/mssql.php
%{php_pear_dir}/MDB2/Driver/Native/mssql.php
%{php_pear_dir}/MDB2/Driver/Reverse/mssql.php
%{php_pear_dir}/MDB2/Driver/mssql.php
%{php_pear_dir}/MDB2/Driver/Function/mssql.php
%{php_pear_dir}/data/%{_pearname}
