Name:		mftrace
Version:	1.2.15
Release:	%mkrel 2
Epoch:		2
Summary:	Generates scalable fonts for TeX
Group:		Publishing
License:	GPL
URL:		http://lilypond.org/mftrace/
Source0:	http://lilypond.org/download/sources/mftrace/mftrace-%{version}.tar.gz
Requires:	autotrace
Requires:	fontforge
Requires:	potrace
Requires:	python
Requires:	t1utils
Requires:	tetex
BuildRequires:	autotrace
BuildRequires:	potrace
BuildRequires:	python
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
%{configure2_5x}
%{make} CC="%{__cc}" CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/gf2pbm
%attr(0755,root,root) %{_bindir}/mftrace
%{_mandir}/man1/mftrace.1*
%{_datadir}/%{name}
