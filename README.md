# check_pdb_hook
Pre-commit hook to check for exposed PDB statements in Python files. Adds functionality to disable strict checking to allow for commenting of debug messages

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/conorfalvey/check_pdb_hook
    rev: 0.0.9
    hooks:
    -   id: check_pdb_hook
```
