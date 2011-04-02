#
# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - fix linking argument order
#  - fix nvidia vs. libXrandr >= 1.2 conflict (nvidia drivers still supports
#    only libXrandr 1.1 - with no gamma support; it causes application crash
#    on XRRSetCrtcGamma function called by SDL_SetVideoMode)
#  - add and/or fix users/groups permissions
#  - split to subpackages?
#  - check how it works with external python libraries
#
# Conditional build:
%bcond_with     external_python
%bcond_without	goom

Summary:	XBMC
Name:		xbmc
Version:	10.1
Release:	0.2
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://www.softliste.de/xbmc/releases/source/%{name}-%{version}.tar.gz
# Source0-md5:	391398126cb86a4f6fbd0b7037997d84
Source1:	goom_icon.png
# Source1-md5:	8c0ffe2055f2cfde1189687d12a68aa8
URL:		http://xbmc.org
Patch0:		%{name}-nobash.patch
Patch1:		%{name}-python27.patch
Patch2:		%{name}-subtitle_tags.patch
Patch3:		%{name}-goom_enable.patch
Patch4:		%{name}-fpsrate.patch
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	enca-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel
BuildRequires:	glew-devel
BuildRequires:	gperf
BuildRequires:	gtk+-devel
BuildRequires:	hal-devel
BuildRequires:	jasper-devel
BuildRequires:	libao-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdts-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	openssl-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
# used internally
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	unzip
BuildRequires:	wavpack-devel
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires:	/usr/bin/glxinfo
Requires:	SDL >= 1.2.14-5
Requires:	lsb-release
Requires:	xorg-app-xdpyinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q
%patch0 -p1
%undos xbmc/lib/libPython/xbmcmodule/xbmcaddonmodule.cpp
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
./bootstrap
%configure \
	--disable-debug \
	--enable-external-libraries \
	--%{?with_external_python:en}%{!?with_external_python:dis}able-external-python \
	--%{?with_goom:en}%{!?with_goom:dis}able-goom
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xbmc/addons/visualization.goom/icon.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_docdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/256x256/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/xsessions/XBMC.desktop
