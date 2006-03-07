%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	DICOM
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - package for reading and modifying DICOM files
Summary(pl):	%{_pearname} - odczyt i modyfikowanie plików DICOM
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e5392bb15f1cdd24cbeec20465c1fced
URL:		http://pear.php.net/package/File_DICOM/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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
DICOM standard can be found at: http://medical.nema.org/.

In PEAR status of this package is: %{_status}.

%description -l pl
File_DICOM pozwala na czytanie i modyfikowanie plików DICOM.

DICOM to skrót od Digital Imaging and COmmunications in Medicine
(cyfrowe obrazy i komunikacja w medycynie) i jest standardem do
tworzenia, przechowywania i przesy³ania cyfrowych obrazów
(prze¶wietleñ, tomografii) oraz powi±zanych informacji u¿ywanych w
medycynie. Ten pakiet akurat nie obs³uguje wymiany/przesy³ania danych
DICOM, ani ¿adnej funkcjonalno¶ci zwi±zanej z sieci±. Wiêcej
informacji o standardzie DICOM mo¿na znale¼æ pod
http://medical.nema.org/.

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
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
