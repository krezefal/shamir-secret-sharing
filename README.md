# Shamir's Secret Sharing

Shamir's Secret Sharing is an algorithm based on the Lagrange 
interpolation theorem using for distributing a secret in such a way that
no individual holds intelligible information about it.

### Usage

The program is a CLI app written in Python 3.10, which does both: the 
generation of shares for a known secret message and the restoring 
(reassembling) this secret using provided shares. Program is implemented
by 2 scripts (`sss-split.py` and `sss-restore.py`), that use the 
functionality from `sss_lib` package.

To split the secret (256 ASCII chars), follow next:
```
python3 sss-split.py -n NUMBER -t THRESHOLD [-h]
```
```
Options:
  -n NUMBER, --number NUMBER
                        Number of shares to be generated.
  -t THRESHOLD, --threshold THRESHOLD
                        Minimum number of shares required to restore a secret secured by SSS.
  -h, --help            Show this help message and exit.

```

For restoring the secret with shares, use:
```
python3 sss-restore.py -t THRESHOLD [-h]
```
```
Options:
  -t THRESHOLD, --threshold THRESHOLD
                        Minimum number of shares required to restore a secret secured by SSS.
  -h, --help            Show this help message and exit.

```
