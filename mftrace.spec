Name:		mftrace
Version:	1.2.19
Release:	2
Summary:	Generates scalable fonts for TeX
Group:		Publishing
License:	GPL
URL:		http://lilypond.org/mftrace/
Source0:	http://lilypond.org/download/sources/mftrace/mftrace-%{version}.tar.gz
Requires:	potrace
Requires:	fontforge
Requires:	potrace
Requires:	python
Requires:	t1utils
Requires:	texlive
BuildRequires:	autotrace
BuildRequires:	potrace
BuildRequires:	python

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
for i in $(find . -name '*.py');do 2to3 -w $i;done

%build
%configure
%make CC="%{__cc}" CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%attr(0755,root,root) %{_bindir}/gf2pbm
%attr(0755,root,root) %{_bindir}/mftrace
%{_mandir}/man1/mftrace.1*
%{_datadir}/%{name}
