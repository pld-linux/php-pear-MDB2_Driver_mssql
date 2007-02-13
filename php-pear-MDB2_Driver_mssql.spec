%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_mssql
%define		_status		alpha
%define		_pearname	MDB2_Driver_mssql

Summary:	%{_pearname} - mssql MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik mssql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	17922dcc2afac4fe146b7911ec2d99c1
URL:		http://pear.php.net/package/MDB2_Driver_mssql/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(mssql)
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 2.0.0-0.beta6
Requires:	php-pear-PEAR-core >= 1:1.0b1
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
