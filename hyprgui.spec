Name:           hyprgui
Version:        0.1.7
Release:        1
Summary:        GUI for configuring Hyprland, written in blazingly fast Rust!
License:        GPL-2.0
Group:          Tools
URL:            https://github.com/hyprutils/
Source0:        https://github.com/hyprutils/hyprgui/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  git
BuildRequires:  rust-packaging
BuildRequires:	rust
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(gtk4)

Requires:  gtk4
Requires:  hyprland

%description
An unofficial GUI for configuring Hyprland, built with GTK4 and Rust.
Comes with a custom hyprparser for Hyprland's configuration file.

%prep
# Vendored sources
%autosetup -n %{name}-%{version} -p1 -a1
%cargo_prep -v vendor
cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release

%install
# Rust is so great and amazing that it doesn't even allow using a simple macro to automatically install compiled files. 
# Don't say rust is great, it's crap from the point of view of a linux distribution, and we're not even talking about distributing libraries as a vendor...

%files
install -Dm0755 -t "%{buildroot}%{_bindir}/" "%{_builddir}/%{name}-%{version}/target/release/"
#install -Dm644 "$pkgname.png" "$pkgdir/usr/share/icons/$pkgname.png"
#install -Dm644 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
