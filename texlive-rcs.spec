# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/rcs
# catalog-date 2007-06-06 17:06:28 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-rcs
Version:	20070606
Release:	1
Summary:	Use RCS (revision control system) tags in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rcs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The rcs package utilizes the inclusion of RCS supplied data in
LaTeX documents. It's upward compatible to *all* rcs styles I
know of. In particular, you can easily - access values of every
RCS field in your document - put the checkin date on the
titlepage - put RCS fields in a footline You can typeset
revision logs. Not in verbatim -- real LaTeX text! But you need
a configurable RCS for that. Refer to the user manual for more
detailed information. You can also configure the rcs package
easily to do special things for any keyword. This bundle comes
with a user manual, an internal interface description, full
documentation of the implementation, style information for AUC-
TeX, and test cases.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rcs/rcs.sty
%doc %{_texmfdistdir}/doc/latex/rcs/CATALOG
%doc %{_texmfdistdir}/doc/latex/rcs/History
%doc %{_texmfdistdir}/doc/latex/rcs/INSTALL
%doc %{_texmfdistdir}/doc/latex/rcs/License
%doc %{_texmfdistdir}/doc/latex/rcs/MANIFEST
%doc %{_texmfdistdir}/doc/latex/rcs/README
%doc %{_texmfdistdir}/doc/latex/rcs/rcs-conf.pdf
%doc %{_texmfdistdir}/doc/latex/rcs/rcs-user.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rcs/Makefile
%doc %{_texmfdistdir}/source/latex/rcs/rcs.el
%doc %{_texmfdistdir}/source/latex/rcs/src/Diff
%doc %{_texmfdistdir}/source/latex/rcs/src/Imakefile
%doc %{_texmfdistdir}/source/latex/rcs/src/README
%doc %{_texmfdistdir}/source/latex/rcs/src/TODO
%doc %{_texmfdistdir}/source/latex/rcs/src/rcs-conf.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/rcs-doc.sty
%doc %{_texmfdistdir}/source/latex/rcs/src/rcs-user.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/rcs.doc
%doc %{_texmfdistdir}/source/latex/rcs/src/style/rcs.el
%doc %{_texmfdistdir}/source/latex/rcs/src/style/rcs.elc
%doc %{_texmfdistdir}/source/latex/rcs/src/test/Imakefile
%doc %{_texmfdistdir}/source/latex/rcs/src/test/Makefile
%doc %{_texmfdistdir}/source/latex/rcs/src/test/empty-log.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/german.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/log-error.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/log.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/rcsdef.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/rcsid-param.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/rcsid.tex
%doc %{_texmfdistdir}/source/latex/rcs/src/test/under_score.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
