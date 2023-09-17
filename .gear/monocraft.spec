%define _unpackaged_files_terminate_build 1
%define fname monocraft

Name: fonts-ttf-%fname
Version: 3.0
Release: alt1

Summary: Monocraft font
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/IdreesInc/Monocraft

BuildArch: noarch

Source: %name-%version.tar
Requires(pre): fontconfig
BuildRequires(pre): python3 fontforge rpm-build-fonts

%description
A monospaced programming font inspired by the Minecraft typeface

%prep
%setup

%build
cd src
python3 monocraft.py

%install
cd dist
%ttf_fonts_install %fname

%files -f dist/%fname.files

%changelog
* Sun Sep 17 2023 Ajrat Makhmutov <ajratma@altlinux.org> 3.0-alt1
- First build for ALT

