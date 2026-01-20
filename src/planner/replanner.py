def replan(tasks, completed_titles):
    return [t for t in tasks if t["title"] not in completed_titles]
