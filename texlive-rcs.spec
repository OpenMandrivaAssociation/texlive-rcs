Name:		texlive-rcs
Version:	20180303
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rcs
%doc %{_texmfdistdir}/doc/latex/rcs
#- source
%doc %{_texmfdistdir}/source/latex/rcs

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
