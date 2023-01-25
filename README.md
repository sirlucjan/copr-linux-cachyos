<div align="center">
 
  <h1 align="center">linux-cachyos-bore for Fedora</h1>
</div>

### linux-cachyos-bore uses as default the BORE scheduler
- BORE (Burst-Oriented Response Enhancer) CPU Scheduler by [firelzrd (BORE)](https://github.com/firelzrd/bore-scheduler)

### Features
- Choose between `LLVM/LTO` or `GCC`.
- Improved BFQ Scheduler.
- Back-ported patches from `linux-next`.
- MEMCG MG LRU Patchset.
- Latency Nice Patchset included usuage with `ananicy-cpp` [feature branch](https://lore.kernel.org/lkml/20220925143908.10846-1-vincent.guittot@linaro.org/T/#t).
- Scheduler patches from linux-next/tip.
- rcu fixes and improvements.
- printk patches.
- BBRv2 tcp_congestion_control.
- Latest & improved ZSTD patch-set.
- Latest BTRFS/XFS/EXT4 improvements & fixes.
- AMD PSTATE EPP Driver enabled by default and with enhancements patches/fixes.
- Clearlinux Patchset.
- Futex fixes and winesync is available.
- UserKSM daemon from pf.

### Checking for the cpu support
Check support by the following the command
```
/lib64/ld-linux-x86-64.so.2 --help | grep "(supported, searched)"

```
If it does not detect x86_64_v3 support do not install the kernel. Otherwise you will end up with a non-functioning operating system! 

### Install drivers for lto kernel
If you build external modules (e.g. for Nvidia graphics card drivers) and use the -lto kernel, you need to install the following dependencies:
```
dnf install clang clang-devel llvm lld
```

