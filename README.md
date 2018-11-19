# limit_visible_cpus

Limit number of CPUs visible to processes on Linux, which use
"sysconf" mechanism to count them.

Uses LD_PRELOAD hooking to overrride results of sysconf call.

## Entry points

 * See get_ncpus.sh and get_ncpus.py for a usage example.
 * Use build.sh to build the library using gcc or clang.
 * Edit hard-coded constant in limit_visible_cpus.c to limit max number of cpus.

## License

Licensed under [MIT License](https://opensource.org/licenses/MIT).
Copyright 2018, Kai Londenberg