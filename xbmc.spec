#
# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - fix linking argument order
#  - fix nvidia vs. libXrandr >= 1.2 conflict (nvidia drivers still supports
#    only libXrandr 1.1 - with no gamma support; it causes application crash
#    on XRRSetCrtcGamma function called by SDL_SetVideoMode)
#  - add and/or fix users/groups permissions
#  - split to subpackages?
#
# Conditional build:
%bcond_without	goom	# build without goom visualisation
%bcond_with	hal			# build with HAL

Summary:	XBMC is a free and open source media-player and entertainment hub
Name:		xbmc
Version:	12.1
Release:	1
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
Source0:	http://mirrors.xbmc.org/releases/source/%{name}-%{version}.tar.gz
# Source0-md5:	8955473f84cb2a0513c0f3efd7e68843
URL:		http://xbmc.org/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
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
%if %{with hal}
BuildRequires:	hal-devel
%endif
BuildRequires:	jasper-devel
BuildRequires:	libass-devel
BuildRequires:	libbluray-devel
BuildRequires:	libcdio-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libogg-devel
BuildRequires:	libplist-devel
BuildRequires:	libpng-devel
BuildRequires:	librtmp-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libssh-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	openssl-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
# used internally
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	tinyxml-devel
BuildRequires:	udev-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	yajl-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
#https://github.com/sahlberg/libnfs
#BuildRequires:	libnfs-devel
#http://sites.google.com/site/alexthepuffin/home
#BuildRequires:	afpfs-ng-devel
#http://mirrors.xbmc.org/build-deps/darwin-libs/libshairport-1.2.0.20310_lib.tar.gz
#https://github.com/albertz/shairport
#BuildRequires: libshairport
#http://www.broadcom.com/support/crystal_hd/
#BuildRequires:	crystalhd-devel
#http://libcec.pulse-eight.com/
#BuildRequires:	libcec-devel >= 1.1.0
Requires:	/usr/bin/glxinfo
Requires:	SDL >= 1.2.14-5
Requires:	lsb-release
Requires:	xorg-app-xdpyinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XBMC media center is a free cross-platform media-player jukebox and
entertainment hub. XBMC can play a spectrum of of multimedia formats,
and featuring playlist, audio visualizations, slideshow, and weather
forecast functions, together third-party plugins.

%prep
%setup -q

%build
./bootstrap
%configure \
	--disable-debug \
	--enable-external-libraries \
	--enable-udev \
	--disable-libcec \
	--disable-libusb \
	--disable-nfs \
	--disable-afpclient \
	--disable-airtunes \
	--disable-crystalhd \
	%{__enable_disable goom} \
	%{__enable_disable hal}

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_docdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/256x256/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/xsessions/XBMC.desktop
