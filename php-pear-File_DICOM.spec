# ToDo:
# - pl description
%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       DICOM
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Package for reading and modifying DICOM files
Summary(pl):	%{_pearname} - manipulacje na plikach DICOM
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_DICOM allows reading and modifying of DICOM files.

DICOM stands for Digital Imaging and COmmunications in Medicine, and
is a standard for creating, storing and transfering digital images
(X-rays, tomography) and related information used in medicine. This
package in particular does not support the exchange/transfer of DICOM
data, nor any network related functionality. More information on the
DICOM standard can be found at: http://medical.nema.org/

This class has in PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
