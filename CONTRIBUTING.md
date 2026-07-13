# Contributing to TaskLite

Thanks for practicing here! This project exists so you can go through a
real fork -> branch -> commit -> push -> pull request cycle safely.

## Before you start

1. Read this file fully.
2. Look at the [Issues](../../issues) tab and pick ONE issue.
3. Comment on the issue saying you're working on it, so two people
   don't accidentally do the same thing.

## Setup

```bash
git clone https://github.com/<your-username>/tasklite.git
cd tasklite
python3 src/tasklite.py list
```

## Making a change

```bash
git checkout -b fix-<short-description>
# make your changes
pytest                     # make sure existing tests still pass
git add .
git commit -m "Fix: <short description>"
git push origin fix-<short-description>
```

Then open a pull request from your fork on GitHub.

## Commit messages

Keep them short and in the present tense: `Fix off-by-one task numbering`,
not `Fixed a bug I found`.

## Code style

Plain, readable Python. No external dependencies. If a function does
something non-obvious, add a one-line docstring.

## What happens after you open a PR

- An automated check (CI) will run the test suite.
- A maintainer will review your change and may ask for edits — that's
  normal, not a rejection.
- Once it looks good, it gets merged.
