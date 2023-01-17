# Chart

This is a self-defined data structure, it can be seen as a 2D chart like:
|               | 0     | 1     |  2  | 3   | 4   | 5   |
|:-------------:|-------|-------|:---:|-----|-----|-----|
|      Name     | Peter | Alice | Tom | Bob | Cat | Dog |
|     Gender    | M     | F     | M   | F   | M   | F   |
| Math_Grade    | 100   | 99    | 30  | 25  | 78  | 91  |
| English_Grade | 101   | 32    | 57  | 11  | 28  | 99  |
The `row_name` of `Chart` are strings, while the `index` are integers, user can access the `Chart` by either `row_name`, `index` and `row_name` with `index`.
## Initialize
```
from utils.chart import Chart

row_names = ['Name','Gender','Math_Grade','English_Grade']
length = 6
chart = Chart(length, row_names)
```
This creates a `Chart` with the specified row_names and specified length. Notice the length of chart is fixed and cannot be modified currently. 

## Access by `row_name`
* Write
    ```
    chart['Math_Grade'] = [100,99,30,25,78,91]
    ```
    Notice the written list's length must equal to `chart.len`(initialized as 6 in this example)
* Read
    ```
    chart['Math_Grade']
    ```
    This will return a list of integers, in the above table, it should be:
    ```
    [100,99,30,25,78,91]
    ```

## Access by `index`
* Write

    ```
    tom_info = {'Name':Tom, 'Gender':'M', 'Math_Grade': 30, 'English_Grade':57}
    chart[2] = tom_info
    ```
    Insert a dict into the chart. Notice that the inserted dict's keys must be a subset of chart's `row_name`, otherwise it will fail.

* Read

    ```
    chart[2]
    ```
    This will return a dict of that column, in the above table, it should be:
    ```
    {'Name':Tom, 'Gender':'M', 'Math_Grade': 30, 'English_Grade':57}
    ```

## Access by `row_name` and `index`
* Read
    ```
    chart['Gender',2]
    ```
    This will return the value at `Gender` row, `index` 2, in the above table, it should be:
    ```
    'M'
    ```