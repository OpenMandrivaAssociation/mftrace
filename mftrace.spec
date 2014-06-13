Name:		mftrace
Version:	1.2.18
Release:	2
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
Requires:	texlive
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


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2:1.2.18-1mdv2012.0
+ Revision: 778490
- Update to latest upstream release.

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2:1.2.16-2mdv2011.0
+ Revision: 612862
- the mass rebuild of 2010.1 packages

* Thu Apr 15 2010 Buchan Milne <bgmilne@mandriva.org> 2:1.2.16-1mdv2010.1
+ Revision: 535079
- update to new version 1.2.16

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2:1.2.15-2mdv2010.0
+ Revision: 430023
- rebuild

* Thu Sep 04 2008 Buchan Milne <bgmilne@mandriva.org> 2:1.2.15-1mdv2009.0
+ Revision: 280493
- update to new version 1.2.15

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2:1.2.14-3mdv2009.0
+ Revision: 252366
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 2:1.2.14-1mdv2008.1
+ Revision: 140953
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 David Walluck <walluck@mandriva.org> 2:1.2.14-1mdv2008.0
+ Revision: 14225
- 1.2.14


* Sun Jan 28 2007 Buchan Milne <bgmilne@mandriva.org> 1.2.9-1mdv2007.0
+ Revision: 114627
- New version 1.2.9
- Updated URLs

* Thu Sep 07 2006 Buchan Milne <bgmilne@mandriva.org> 2:1.2.4-2mdv2007.0
+ Revision: 60244
- (minor) fix misplaced change
- fix idiotic epoch

* Mon Sep 04 2006 Buchan Milne <bgmilne@mandriva.org> 1:1.2.4-1mdv2007.0
+ Revision: 59677
- New version 1.2.4

* Fri Aug 11 2006 Bruno Cornec <Bruno.Cornec@mandriva.org> 2:1.1.17-2mdv2007.0
+ Revision: 55360
- release and Epoch put in line
- mftrace now uses %%mkrel
  Epoch increased
- import mftrace-1.1.17-1mdk

* Sun Oct 30 2005 Abel Cheung <deaddog@mandriva.org> 1.1.17-1mdk
- New release 1.1.17

* Wed Aug 17 2005 Abel Cheung <deaddog@mandriva.org> 1.1.16-1mdk
- New release 1.1.16

* Thu Aug 11 2005 Abel Cheung <deaddog@mandriva.org> 1:1.1.12-1mdk
- Revert to 1.1.12, lilypond won't build with 1.1.13

* Thu Aug 11 2005 Abel Cheung <deaddog@mandriva.org> 1.1.13-2mdk
- Rebuild

* Sun Aug 07 2005 Abel Cheung <deaddog@mandriva.org> 1.1.13-1mdk
- New release 1.1.13
- Fix build dependency

* Sat Aug 06 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.8-2mdk
- rebuilt against latest libMagick

* Sun Apr 17 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.1.8-1mdk
- Release: 1.1.8.

* Mon Mar 21 2005 Abel Cheung <deaddog@mandrake.org> 1.1.6-1mdk
- New release 1.1.6

* Sat Feb 05 2005 Abel Cheung <deaddog@mandrake.org> 1.1.2-2mdk
- Requires fontforge instead of pfaedit

* Sun Jan 16 2005 Abel Cheung <deaddog@mandrakesoft.com> 1.1.2-1mdk
- New release 1.1.2

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 1.0.36-2mdk
- Requires python

* Fri Dec 10 2004 Abel Cheung <deaddog@mandrake.org> 1.0.36-1mdk
- New version
- Pulls in potrace too, in case some software wants --autotrace option
  and others want --potrace option

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 1.0.33-2mdk
- Please use configure2_5x whenever possible
- Fix BuildRequires

* Sun Jul 18 2004 Michael Scherer <misc@mandrake.org> 1.0.33-1mdk
- New release 1.0.27

