%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_mssql
%define		_status		alpha
%define		_pearname	MDB2_Driver_mssql

Summary:	%{_pearname} - mssql MDB2 driver
Summary(pl):	%{_pearname} - sterownik mssql dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	219487ade12e22b709296d45c9dded5a
URL:		http://pear.php.net/package/MDB2_Driver_mssql/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.3.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0-0.beta6
Requires:	php-mssql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Microsoft SQL Server MDB2 driver.
 
In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik Microsoft SQL Server dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

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
%{php_pear_dir}/package_mssql.php
