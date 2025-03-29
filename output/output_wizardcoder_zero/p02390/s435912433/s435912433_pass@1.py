```python
time_in_seconds = int(input())
hours, remainder = divmod(time_in_seconds, 360*60)
minutes, seconds = divmod(remainder, 60)
print("{}:{:02d}:{:02d}".format(hours, minutes, seconds))
```