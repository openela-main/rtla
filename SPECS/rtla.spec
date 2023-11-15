Name:    rtla
Version: 5.14.0
Release: 8%{?dist}
Summary: Real-Time Linux Analysis tools

License: GPLv2
URL:     https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
# The Source0 rtla-5.14.0.tar.bz2 file was created from git
# tag kernel-5.14.0-204.el9
# and from the tools/tracing/rtla directory issuing make tarball
Source0: rtla-5.14.0.tar.bz2

BuildRequires: gcc
BuildRequires: python3-docutils
BuildRequires: libtraceevent-devel >= 1.5.3
BuildRequires: libtracefs-devel >= 1.3.1
Requires: libtraceevent >= 1.5.3
Requires: libtracefs >= 1.3.1

# Patches
Patch1: rtla-Fix-exit-status-when-returning-from-calls-to-usage.patch
Patch2: Documentation-rtla-Correct-command-line-example.patch
Patch3: tools-tracing-rtla-osnoise_hist-use-total-duration-f.patch
Patch4: tools-tracing-rtla-osnoise_hist-display-average-with.patch
Patch5: rtla-timerlat-Add-auto-analysis-core.patch
Patch6: rtla-timerlat-Add-auto-analysis-support-to-timerlat.patch
Patch7: rtla-timerlat-Add-auto-analysis-only-option.patch
Patch8: rtla-timerlat-Fix-Previous-IRQ-auto-analysis-line.patch
Patch9: Documentation-rtla-Add-timerlat-top-auto-analysis-op.patch
Patch10: rtla-Add-hwnoise-tool.patch
Patch11: Documentation-rtla-Add-hwnoise-man-page.patch

%description
The rtla meta-tool includes a set of commands that aims to analyze
the real-time properties of Linux. Instead of testing Linux as a black box,
rtla leverages kernel tracing capabilities to provide precise information
about the properties and root causes of unexpected results.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1


%build
%make_build


%install
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 rtla %{buildroot}/%{_bindir}/rtla
install -d -m 755 %{buildroot}/%{_mandir}
make DESTDIR=%{buildroot} -C Documentation clean
make DESTDIR=%{buildroot} -C Documentation
make DESTDIR=%{buildroot} -C Documentation install
(cd %{buildroot}

        ln -sf rtla ./%{_bindir}/osnoise
        ln -sf rtla ./%{_bindir}/timerlat
)


%files
%{_bindir}/rtla
%{_bindir}/osnoise
%{_bindir}/timerlat
%doc
%{_mandir}/man1/rtla-osnoise-hist.1.gz
%{_mandir}/man1/rtla-osnoise-top.1.gz
%{_mandir}/man1/rtla-osnoise.1.gz
%{_mandir}/man1/rtla-timerlat-hist.1.gz
%{_mandir}/man1/rtla-timerlat-top.1.gz
%{_mandir}/man1/rtla-timerlat.1.gz
%{_mandir}/man1/rtla.1.gz
%{_mandir}/man1/rtla-hwnoise.1.gz


%changelog
* Fri Jul 14 2023 John Kacur <jkacur@redhat.com> - 5.14.0-8
- Add rtla hwnoise
Resolves: bz2175295
jiraProject ==  RHELPLAN-150659

* Fri Jul 14 2023 John Kacur <jkacur@redhat.com> - 5.14.0-7
- Add rtla timerlat auto analysis
Resolves: rhbz#2175292
jiraProject == RHELPLAN-150657

* Tue May 09 2023 John Kacur <jkacur@redhat.com> - 5.14.0-6
- Forward port the tests directory for ci testing
Resolves: rhbz#2196611
jiraProject == RHELPLAN-156801

* Fri May 05 2023 John Kacur <jkacur@redhat.com> - 5.14.0-5
- Correct commandline example
Resolves: rhbz#2189440
jiraProject ==  RHELPLAN-155623

* Thu Jan 26 2023 John Kacur <jkacur@redhat.com> - 5.14.0-4
- Add a gating test for rtla
Resolves: rhbz#2164877
jiraProject == RHELPLAN-146610

* Thu Jan 26 2023 John Kacur <jkacur@redhat.com> - 5.14.0-3
- Fix exit status when returning from calls to usage()
Resolves: rhbz#2161423
jiraProject == RHELPLAN-145250

* Tue Dec 13 2022 John Kacur <jkacur@redhat.com> - 5.14.0-2
- A few spec file improvements
Resolves: rhbz#2075203
jiraProject == RHELPLAN-142262

* Wed Dec 07 2022 John Kacur <jkacur@redhat.com> - 5.14.0-1
- Initial build of rtla
