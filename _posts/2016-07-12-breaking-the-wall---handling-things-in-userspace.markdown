---
layout: post
title:  "Breaking the Wall - Handling Things in Userspace"
date:   2016-07-12 16-00-00 +0300
categories: meetups
---
[meetup event](https://www.meetup.com/Tel-Aviv-Yafo-Linux-Kernel-Meetup/events/232058698/)

This time we'll talk about recent trends in moving handling of system-level
events to userspace to achieve more flexible systems. We'll see how the
traditional Unix separation of mechanism and policy is being extended to
interrupt and page fault handling.

Page faults and migrations

userfaultfd is a (relatively) new set of kernel features that allows us to
handle page faults in userspace. It is used to implement migration in KVM/Qemu
and CRIU. Mike Rapoport will describe the userfaultfd mechanisms and their
usage for implementation of post-copy migration. In addition, Mike will
address current limitations of userfaultfd, particularly when it is used in
non-cooperative mode.

  
Linux interrupt handling

In this talk Liran will discuss interrupt management in Linux, effective
handling, how to defer work using tasklets, workqueues and timers. We'll learn
how to handle interrupts in userspace and talk about the performance and
latency aspects of each method as well as look at some examples from the
kernel source.

Schedule:

19:00-19:15 mingling

19:15-20:00 userfaultfd and post-copy migration of VMs and containers

20:00-20:15 break

20:15-21:00 Linux interrupt handling

Liran Ben Haim

Liran is the CTO at Mabel technology and co-founder of DiscoverSDK - Software
Libraries directory and DiscoverCloud - Business Apps directory

More than 20 years of training experience including courses in: Linux,
Android, Real-time and Embedded systems, and many more.

Mabel technology -[<http://www.mabel-tech.com/>](http://www.mabel-tech.com/)

DiscoverSDK -[<http://www.discoversdk.com/>](http://www.discoversdk.com/)

DiscoverCloud -
[<http://www.discovercloud.com/>](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.discovercloud.com%2F&h=9AQEsn30U&enc
=AZPUpMbgdmnS1Poi8RRQQGZERLy1C9cYOUNM-ObhRlOgYP7E5o9sr1aPSMU3C61gVI4&s=1)

We are always looking for new speakers and ideas to improve our growing
community. We are also looking for new venues for our future meetups. If you
have any suggestions don't hesitate to contact us!

