# TASK MANAGER

## Install

Use **pip** to install the latest stable version of `task-manager`:

```
$ pip install task-manager
```

## How to use
in tasks.py
```python
from task_manager.services import TaskManager

@task(name='get_urls')
def get_urls():
    go = TaskManager(name='get_urls')
    if go.start() is True:
        go.close()
        return 'ok'
    else:
        return 'lock'
```