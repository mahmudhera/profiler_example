# profiler_example

Examples on how to run a profiler to find bottlenecks in a python code.


## Function profiler: `cProfile`

### How to install
Does not require installation

### How to run
```
python -m cProfile -s cumulative main.py 45
```

### How to interpret the outputs

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      7/1    0.000    0.000    5.035    5.035 {built-in method builtins.exec}
        1    0.000    0.000    5.035    5.035 main.py:1(<module>)
        1    0.000    0.000    5.034    5.034 main.py:15(main)
        5    0.000    0.000    5.026    1.005 main.py:4(slow_function)
        5    5.025    1.005    5.025    1.005 {built-in method time.sleep}
      9/2    0.000    0.000    0.008    0.004 <frozen importlib._bootstrap>:1022(_find_and_load)
      9/2    0.000    0.000    0.008    0.004 <frozen importlib._bootstrap>:987(_find_and_load_unlocked)
        1    0.000    0.000    0.008    0.008 argparse.py:1694(__init__)
      9/2    0.000    0.000    0.008    0.004 <frozen importlib._bootstrap>:664(_load_unlocked)
      6/2    0.000    0.000    0.008    0.004 <frozen importlib._bootstrap_external>:877(exec_module)
        2    0.000    0.000    0.008    0.004 argparse.py:1392(add_argument)
        2    0.000    0.000    0.007    0.004 argparse.py:2546(_get_formatter)
        2    0.000    0.000    0.007    0.004 argparse.py:161(__init__)
     12/2    0.000    0.000    0.007    0.004 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
        1    0.000    0.000    0.007    0.007 shutil.py:1(<module>)
        9    0.000    0.000    0.005    0.001 <frozen importlib._bootstrap>:564(module_from_spec)
        3    0.000    0.000    0.005    0.002 <frozen importlib._bootstrap_external>:1174(create_module)
        3    0.005    0.002    0.005    0.002 {built-in method _imp.create_dynamic}
        1    0.000    0.000    0.002    0.002 bz2.py:1(<module>)
        1    0.000    0.000    0.002    0.002 lzma.py:1(<module>)
        9    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:921(_find_spec)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:950(get_code)
        9    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1431(find_spec)
        9    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1399(_get_spec)

```

It means that the program needed 5.035s to run, of which, 5.026s was spent in slow_function. This is the bottleneck.

## Line profiler: `line_profiler`
The above function profiler `cProfile` allows us to investigate at the function level. The resolution is at the function calls, not the individual lines. Now we need to profile at the lines too, to see what line in the slow_function is causing the slowdown.

### How to install
```
conda install line_profiler
```

### How to run
Before the function we want to profile, we need to write `@profile`.

Then:
```
kernprof -l -v main.py 45
```

Profiling stats will be stored in main.py.lprof

### How to interpret results
Very intuitive. %time is the most useful column. To view the results:
```
python -m line_profiler main.py.lprof
```
