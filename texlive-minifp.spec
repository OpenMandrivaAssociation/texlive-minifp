%global tl_name minifp
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.96
Release:	%{tl_revision}.1
Summary:	Fixed-point real computations to 8 decimals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/minifp
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides basic arithmetic operations to 8 decimal places for
plain TeX or LaTeX. Results are exact when they fit within the digit
limits. Along with the basic package is an optional extension that adds
computation of sin, cos, log, sqrt, exp, powers and angles. These are
also exact when theoretically possible and are otherwise accurate to at
least 7 decimal places. In addition, the package provides a stack-based
programming environment.

