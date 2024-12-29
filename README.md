# Multiple sendevent calls in one command 

Tested against BlueStacks 5, should work on any rooted Android system, and Linux systems in general

## To write "hello" using 19 commands

If you want to write 'hello' using Android's sendevent, you usually need something like this:

```sh
sendevent /dev/input/event3 1 35 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 35 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 18 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 18 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 0
sendevent /dev/input/event3 0 0 0
```

This is slow, because you have to execute 19 times the sendevent command.

## To write "hello" in one single command

### Compile the code 

```sh
g++ -std=c++2a -O3 -g0 sendeventall.cpp
```

### Use 

```sh
./a.out /dev/input/event3 KEY_H:ud:1#KEY_E:ud:0#KEY_L:ud:0#KEY_L:ud:0#KEY_O:ud:0

or 

./a.out /dev/input/event3 35:ud:1#18:ud:0#38:ud:0#38:ud:0#24:ud:0
```

### or the Python wrapper
```py
sendkeycmd = create_sendkey_command(
    exefile="/data/data/com.termux/files/home/sendevent_multicommands_type_text/a.out",
    device_path="/dev/input/event1",
    text="This is a Test!!! REALLY!!!",
    min_time_key_press=1,
    max_time_key_press=3,
)
print(sendkeycmd)

# output:
/data/data/com.termux/files/home/sendevent_multicommands_type_text/a.out /dev/input/event1 KEY_LEFTSHIFT:d:0#KEY_T:ud:1#KEY_LEFTSHIFT:u:0#KEY_H:ud:1#KEY_I:ud:1#KEY_S:ud:3#KEY_SPACE:ud:2#KEY_I:ud:1#KEY_S:ud:3#KEY_SPACE:ud:1#KEY_A:ud:1#KEY_SPACE:ud:1#KEY_LEFTSHIFT:d:0#KEY_T:ud:3#KEY_LEFTSHIFT:u:0#KEY_E:ud:2#KEY_S:ud:1#KEY_T:ud:2#KEY_LEFTSHIFT:d:0#KEY_1:ud:3#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_1:ud:1#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_1:ud:3#KEY_LEFTSHIFT:u:0#KEY_SPACE:ud:2#KEY_LEFTSHIFT:d:0#KEY_R:ud:1#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_E:ud:3#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_A:ud:1#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_L:ud:2#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_L:ud:1#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_Y:ud:3#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_1:ud:3#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_1:ud:1#KEY_LEFTSHIFT:u:0#KEY_LEFTSHIFT:d:0#KEY_1:ud:3#KEY_LEFTSHIFT:u:0

```


#### Explanation - Token: KEY_H:ud:1 / 35:ud:1

```sh
# Tokens are split by "#"

KEY_H or 35 -> keycode "h" (all key codes are available in the source code [linux standard] )
ud -> up and down events - press and release
1 -> sleep 1 ms 
```

#### Explanation - Token: KEY_E:ud:0 / 18:ud:0

```sh
KEY_E or 18 -> keycode "e" 
ud -> up and down events  - press and release
0 -> sleep 0 ms 

Console (stderr) output:

sendevent /dev/input/event3 1 35 1
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 35 0
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 18 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 18 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 0
sendevent /dev/input/event3 0 0 0
```

## To write "Hello" (first letter upper case) in one command

```sh
./a.out /dev/input/event3 KEY_LEFTSHIFT:d:1#KEY_H:ud:1#KEY_LEFTSHIFT:u:1#KEY_E:ud:0#KEY_L:ud:0#KEY_L:ud:0#KEY_O:ud:0
```

### Explanation - Tokens

```sh
KEY_LEFTSHIFT:d:1

KEY_LEFTSHIFT -> press "KEY_LEFTSHIFT" 
d -> down event 
1 -> sleep 1 ms 

KEY_H:ud:1

KEY_H -> press and release "h"
ud -> up and down events 
1 -> sleep 1 ms 

KEY_LEFTSHIFT:u:1

KEY_LEFTSHIFT -> release "KEY_LEFTSHIFT" 
u -> up event 
1 -> sleep 1 ms 

sendevent /dev/input/event3 1 42 1
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 35 1
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 35 0
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 42 0
sendevent /dev/input/event3 0 0 0
sleeping 1 ms
sendevent /dev/input/event3 1 18 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 18 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 38 0
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 1
sendevent /dev/input/event3 0 0 0
sendevent /dev/input/event3 1 24 0
sendevent /dev/input/event3 0 0 0
```