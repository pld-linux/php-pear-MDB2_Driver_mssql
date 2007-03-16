%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_mssql
%define		_status		stable
%define		_pearname	MDB2_Driver_mssql

Summary:	%{_pearname} - mssql MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik mssql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3e10b10da97d118efc93f707119bd675
URL:		http://pear.php.net/package/MDB2_Driver_mssql/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(mssql)
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.4.0
Requires:	php-pear-PEAR-core >= 1:1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Microsoft SQL Server MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik Microsoft SQL Server dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/data/MDB2_Driver_mssql/package_mssql.xml

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
