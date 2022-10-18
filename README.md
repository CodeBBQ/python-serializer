# Python-Serializer

Serialize code blocks over multiple asynchronized processes, with a simple with-statement.


### Example

````python
# Process1: If channel drive is not blocked
>>> with serializer('drive'):
...     sleep(10)
...     print("This process blocks drive.")
Channel drive is available.
This process blocks drive.

# Process2: As process 1 is already running:
>>> with serializer('drive'):
...     print("This must wait until process1 has finished and will block drive for others.")
Channel drive blocked with 1 processes. Waiting 10 seconds.
````

### Install
Download repository and use `pip install`
