# revision 32559
# category Package
# catalog-ctan /macros/generic/minifp
# catalog-date 2014-01-04 14:18:29 +0100
# catalog-license lppl1.3
# catalog-version 0.96
Name:		texlive-minifp
Version:	0.96
Release:	3
Summary:	Fixed-point real computations to 8 decimals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/minifp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides basic arithmetic operations to 8 decimal
places for plain TeX or LaTeX. Results are exact when they fit
within the digit limits. Along with the basic package is an
optional extension that adds computation of sin, cos, log,
sqrt, exp, powers and angles. These are also exact when
theoretically possible and are otherwise accurate to at least 7
decimal places. In addition, the package provides a stack-based
programing environment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/minifp/mfpextra.tex
%{_texmfdistdir}/tex/generic/minifp/minifp.sty
%doc %{_texmfdistdir}/doc/generic/minifp/README
%doc %{_texmfdistdir}/doc/generic/minifp/minifp.pdf
%doc %{_texmfdistdir}/doc/generic/minifp/test1.tex
%doc %{_texmfdistdir}/doc/generic/minifp/test2.tex
#- source
%doc %{_texmfdistdir}/source/generic/minifp/minifp.dtx
%doc %{_texmfdistdir}/source/generic/minifp/minifp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
