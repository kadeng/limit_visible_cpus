#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>

long int sysconf (int parameter) {
	long int (*old_sysconf)(int);
	long int result;
	old_sysconf = dlsym(RTLD_NEXT, "sysconf");
	long int real_result = old_sysconf(parameter);
	if (parameter==_SC_NPROCESSORS_ONLN) {
		return (real_result > 10 ? 10 : real_result);		
	} else {
		return real_result;
	}
}
