%define oname haml

Name:       rubygem-%{oname}
Version:    3.0.24
Release:    2
Summary:    An elegant, structured XHTML/XML templating engine
Group:      Development/Ruby
License:    GPLv2+
URL:        https://haml-lang.com/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(fssm) = 0.1.4
Suggests:   rubygem(maruku)
Suggests:   rubygem(yard)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or
XML
that's designed to express the structure of XHTML or XML documents
in a non-repetitive, elegant, easy way,
using indentation rather than closing tags
and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails,
but it can function as a stand-alone templating engine.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

#Don’t use vendor
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/vendor

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/haml
%{_bindir}/html2haml
%{_bindir}/sass
%{_bindir}/css2sass
%{_bindir}/sass-convert
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.yardopts
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/extra/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/rails/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/init.rb
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CONTRIBUTING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/REVISION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION_NAME
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 3.0.24-1mdv2011.0
+ Revision: 623120
- import rubygem-haml

