#
# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - fix linking argument order
#  - add and/or fix users/groups permissions
#  - split to subpackages?
#
# Conditional build:
%bcond_without	cec	# build without cec support
%bcond_without	goom	# build without goom visualisation
%bcond_with	hal	# build with HAL

Summary:	XBMC is a free and open source media-player and entertainment hub
Name:		xbmc
Version:	12.2
Release:	3
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
Source0:	http://mirrors.xbmc.org/releases/source/%{name}-%{version}.tar.gz
# Source0-md5:	489f3877decae4e265ece54f9eaef0ba
Patch0:		ffmpeg2.patch
URL:		http://xbmc.org/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	OpenGL-devel
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
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	jasper-devel
BuildRequires:	jre
BuildRequires:	libass-devel
BuildRequires:	libbluray-devel >= 0.2.1
BuildRequires:	libcap-devel
BuildRequires:	libcdio-devel
%{?with_cec:BuildRequires:	libcec-devel}
%ifarch i686 pentium4 athlon %{x8664}
BuildRequires:	libcrystalhd-devel
%endif
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
BuildRequires:	libva-glx-devel
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
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
# used internally
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	swig
BuildRequires:	taglib-devel >= 1.8
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
%patch0 -p1

%build
./bootstrap
%configure \
	--disable-debug \
	--enable-external-libraries \
	--enable-pulse \
	--enable-udev \
	--disable-libusb \
	--disable-nfs \
	--disable-afpclient \
	--disable-airtunes \
	%{__enable_disable goom} \
	%{__enable_disable hal} \
	%{__enable_disable libcec}

LIBS="-lpthread"
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
