# Kobayashi

Kobayashi is a space battle simulator designed around the core rules of the
popular role playing game Stars Without Number.

# Usage

To run the sim, simply type `./run_sim.py` and you'll be dropped into an
interactive IPython terminal that has all of the game objects loaded.

```bash
┬─[zoe@fillory:~/Dropbox/Projects/kobayashi]─[10:24:29 AM]
╰─>$ ./run_sim.py 
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

┬─[zoe@fillory:.../Dropbox/Projects/kobayashi]-[Tue Sep 12 10:24:47 2017]
╰─>$ 
```

Type `help()` to be shown the commands available to you.

```python
┬─[zoe@fillory:.../Dropbox/Projects/kobayashi]-[Tue Sep 12 10:35:12 2017]
╰─>$ help()
Out[1]:
{'arena': dict,
 'framenum': int,
 'get_fleet': method,
 'help': method,
 'list_ships': method,
 'load': <function __main__.main.<locals>.load>,
 'num_ships_left': method,
 'register_ship': method,
 'save': <function __main__.main.<locals>.<lambda>>,
 'send_fleet_command': method,
 'ship_by_name': method,
 'ships': list,
 'show': method,
 'tick': method,
 'tickn': method,
 'update_fleet_attr': method}
```
