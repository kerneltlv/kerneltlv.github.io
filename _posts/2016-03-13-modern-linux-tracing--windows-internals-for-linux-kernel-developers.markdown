---
layout: post
title:  "Modern Linux Tracing & Windows internals for linux kernel developers"
date:   2016-03-13 17-00-00 +0200
categories: meetups
---
[meetup event](https://www.meetup.com/Tel-Aviv-Yafo-Linux-Kernel-Meetup/events/229208185/)

Its time for yet another exciting meetup session!  
The lectures in this session will be given by **Sasha Goldshtein**.  
Sasha is the CTO of Sela Group, a training and consulting company based in
Israel that employs over 400 developers world-wide. Most of Sasha's work
revolves around performance optimization, production debugging, and low-level
system diagnostics, but he also dabbles in mobile application development on
iOS and Android. Sasha is the author of two books and three Pluralsight
courses, and a contributor to multiple open-source projects. He blogs at
[<http://blog.sashag.net>](http://blog.sashag.net/).

  
This time our meetup is hosted by Checkpointat their office in Tel Aviv.  
The event will be held at a conference room on the ground floor (Pink
conference room).

  
Brief:  
In this meetup we will talk about Modern tracing and Windows internals.  
Tracing is one of the most important debugging tools for kernel development.
The tracing mechanisms in kernel are getting a lot of new features. I
recommend that you try and think on debugging issues that you had while
developing in the kernel and see how the new tracing features can help you.  
The windows internals lecture will give an interesting overview of how the
things that we all know and love in the linux kernel are implemented in
windows.

  
The schedule for this meetup is:  
19:00-19:15 mingling time  
19:15-20:15 Modern Linux Tracing Landscape (Lecture + Q&amp;A)  
20:15-20:25 break  
20:25-21:25 Windows Internals for Linux Kernel Developers (Lecture + Q&amp;A)

**Modern Linux Tracing Landscape**

The Linux kernel has multiple "tracers" built-in, with various degrees of
support for aggregation, dynamic probes, parameter processing, filtering,
histograms, and other features. Starting from the venerable ftrace, introduced
in kernel 2.6, all the way through eBPF, which is still under development,
there are many options to choose from when you need to statically instrument
your software with probes, or diagnose issues in the field using the system's
dynamic probes. Modern tools include SystemTap, SysDig, ktap, perf, bcc, and
others. In this talk, we will begin by reviewing the modern tracing landscape
-- ftrace, perf_events, kprobes, uprobes, eBPF -- and what insight into system
activity these tools can offer. Then, we will look at specific examples of
using tracing tools for diagnostics: tracing a memory leak using low-overhead
kmalloc/kfree instrumentation, diagnosing a CPU caching issue using perf stat,
probing network and block I/O latency distributions under load, or merely
snooping user activities by capturing terminal input and output.

**Windows Internals for Linux Kernel Developers**

The Windows kernel has a honorable history of more than a quarter of a
century. Since its inception in 1989, Windows NT supported a variety of modern
OS features -- symmetric multiprocessing, interrupt prioritization, virtual
memory, deferred interrupt processing, and many others. In this talk, targeted
for Linux kernel developers, we will highlight the key features of the Windows
NT kernel that are interesting or different from Linux's perspective. We will
begin with a brief overview of processes, threads, and virtual memory on
Windows. Next, we will talk about interrupt handling, interrupt priorities
(IRQLs), bottom-half processing (DPC, APC, kernel worker threads, kernel
thread pool), and I/O request flow. Among other things, we will look at device
driver structure on Windows, application to driver communication (handles,
IOCTLs), and the logical \DosDevices filesystem. Finally, we will discuss some
features introduced in newer Windows versions, such as user-mode drivers
(UMDF).

Notes:  
\- The lectures will be filmed and the video will be uploaded to youtube
(subscribe to kerneltlv channel on youtube!)  
\- The lectures will start at the specified hours so please don't be late.  
\- All the lectures will be in Hebrew.

P.S  
I'm always looking for new lectures so if you think you have what it takes and
want to give a lecture at when of our meetups just let me know :)

And as always I am waiting to see all of you guys. If I'm lucky maybe even see
a few new faces.

Cheers,  
Kfir.

