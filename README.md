# limit_visible_cpus

Limit number of CPUs visible to processes on Linux, which use
"sysconf" mechanism to count them.

Uses LD_PRELOAD hooking to overrride results of sysconf call.

## Requirements

Linux, tested on Ubuntu 16.04, x86-64

## Installation

On Linux, x86-64 systems, please install them like this:

    git clone https://github.com/kadeng/limit_visible_cpus
    cd limit_visible_cpus
    sudo pip install py3nvml
    sudo cp -av dist/bin/* /usr/local/bin/

The lpython scripts from dist/bin dynamically allocate a multiple of
8 cpus and 1 gpu based on current load, and then start a process
limited to just these CPUs and gpus. 

## Entry points in code

 * Use build.sh to build the library using gcc.
 * See get_ncpus.sh and get_ncpus.py for a minimal usage example.
 * Use OMP_NUM_THREADS environment variable to set the number of visible CPUs
 * See dynamic_cpu_and_gpu_limit.py for a complete script which automates all of this and combines
   it with dynamic CPU allocation and affinity setting via taskset

## License

Licensed under [MIT License](https://opensource.org/licenses/MIT).
Copyright 2018, Kai Londenberg
