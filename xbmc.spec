#
# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - fix linking argument order
#  - fix install - add DESTDIR support
#  - don't put binary in %{_datadir} and fix start scripts
#
Summary:	XBMC
Name:		xbmc
Version:	9.11
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/project/xbmc/XBMC%20Source%20Code/Camelot%20-%209.11/%{name}-%{version}.tar.gz
# Source0-md5:	9a68ac1e2f44a54cc3803fcdb1265767
URL:		http://xbmc.org
Patch0:		%{name}-nobash.patch
Patch1:		%{name}-libpng14.patch
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
BuildRequires:	esound-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
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
BuildRequires:	libmms-devel
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
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
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
Requires:	lsb-release
Requires:	xorg-app-xdpyinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./bootstrap
%configure \
	--disable-debug \
	--enable-external-libraries \
	--enable-external-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/xbmc.bin
%attr(755,root,root) %{_datadir}/%{name}/xbmc-xrandr
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/xsessions/XBMC.desktop
