%global debug_package   %{nil}
%global commit          91ae5f88a67b14891cfd43895b01164f6c120420
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global provider        gopkg
%global provider_tld    in
%global repo            check
%global version         v1
%global import_path     %{provider}.%{provider_tld}/%{repo}.%{version}
%global import_path_sec launchpad.net/gocheck

Name:           golang-gopkg-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Rich testing for the Go language
License:        BSD
# gopkg.in/check.v1
URL:            http://%{import_path}
Source0:        https://github.com/go-%{repo}/%{repo}/archive/%{commit}/%{repo}-%{commit}.tar.gz
Obsoletes:	golang-launchpad-gocheck
ExclusiveArch:	%{ix86} x86_64 %{arm}

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path_sec}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{import_path}.

%prep
%setup -n %{repo}-%{commit} -q

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path_sec}/

%check
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc LICENSE README.md
# once src/gopkg.in gets into golang package, remove the line bellow
%dir %{gopath}/src/gopkg.in
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go
%dir %{gopath}/src/launchpad.net
%dir %{gopath}/src/%{import_path_sec}
%{gopath}/src/%{import_path_sec}/*.go

%changelog
* Fri Oct 10 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-1
- First package for Fedora
