%undefine _debugsource_packages
Name:           hyprgui
Version:        0.1.9
Release:        1
Summary:        GUI for configuring Hyprland, written in CRAPPY bad Rust!
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
# Don't say rust is great, it's crap from the point of view of a linux distribution, and we're not even talking about distributing libraries as a vendor... because this is even worse!

install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 ./%{name}.png %{buildroot}%{_datadir}/icons/%{name}.png
install -Dm0644 ./%{name}.svg %{buildroot}%{_datadir}/icons/%{name}.svg
install -Dm0644 ./%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.*
