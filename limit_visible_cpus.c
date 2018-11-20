#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>
#include <stdlib.h>     /* atoi */

long int sysconf (int parameter) {
	long int (*old_sysconf)(int);
	long int result;
	old_sysconf = dlsym(RTLD_NEXT, "sysconf");
	long int real_result = old_sysconf(parameter);
	if (parameter==_SC_NPROCESSORS_ONLN) {
		char *omp_num_threads = getenv("OMP_NUM_THREADS");
		if (omp_num_threads==NULL) {
			return real_result;
		} else {
			int max_threads = atoi(omp_num_threads);
			if (max_threads>0 && max_threads<300) {
				return (real_result > max_threads ? max_threads : real_result);
			}
		}
	}
	return real_result;
}
