import argparse
import subprocess
from typing import Optional
from typing import Sequence


def check_pdb_hook(files: Sequence[str], strict: bool = False) -> int:
    filtered_files = set(files)

    ret_val = 0
    for filename in filtered_files:
        check = subprocess.run(
            ['grep', 'pdb.set_trace', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            encoding='utf-8',
            # check=True
        )
        pdb_instances = [i for i in check.stdout.split('\n') if i]
        if strict and pdb_instances:
            print(f'{filename} has instance of PDB call. (Strict mode)')
            ret_val = 1
            continue
        for instance in pdb_instances:
            octothorpe_idx = instance.find('#')
            if octothorpe_idx == -1 or octothorpe_idx > instance.find('pdb.set_trace'):
                print(f'{filename} contains exposed PDB statements')
                ret_val = 1
    return ret_val


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'files',
        nargs='*',
        help='Files pre-commit believes are changed.',
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Strict enforcement strips commented instances as well as exposed instances',
    )
    args = parser.parse_args(argv)
    return check_pdb_hook(args.files, args.strict)


if __name__ == '__main__':
    raise SystemExit(main())
