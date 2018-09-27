# Setup

```
pip3 install pelican markdown pelican-alias
```

# Publish

You can either upload with SSH (purely upload new/updated files) or synchronize
with rsync (deleted unnecessary files). For either, set `SSH_USER` in
`./Makefile`. Then run `make publish` followed by either `make ssh_upload` or
`make rsync_upload`.
