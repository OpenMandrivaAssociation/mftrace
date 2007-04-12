%define version 1.2.9
%define rel		1
%define release %mkrel %{rel}

Name:		mftrace
Version:	%{version}
Release:	%{release}
Epoch:		2
Summary:	Generates scalable fonts for TeX
Group:		Publishing
License:	GPL
URL:		http://lilypond.org/mftrace/
Source0:	http://lilypond.org/download/sources/mftrace/mftrace-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	autotrace
BuildRequires:	potrace
Requires:	python
Requires:	tetex
Requires:	autotrace
Requires:	potrace
Requires:	t1utils
Requires:	fontforge >= 1.0-0.040215.1mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mftrace is a small Python program that lets you trace a TeX bitmap
font into a PFA or PFB font (A PostScript Type1 Scalable Font) or TTF
(TrueType) font. It is licensed under the GNU GPL.

Scalable fonts offer many advantages over bitmaps, as they allow
documents to render correctly at many printer resolutions. Moreover,
Ghostscript can generate much better PDF, if given scalable PostScript
fonts.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}



