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
cargo install

%files
